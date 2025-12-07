import pytest

from app.tests.phase_a.data_generator import create_item, create_purchase, create_sale


def _seed_item_with_stock(client, low_stock_threshold: int = 4):
    """Create an item with an initial purchase so analytics tests can run."""
    item = create_item(client, name="Analytics Widget", sku="ANL-001", low_stock_threshold=low_stock_threshold)
    create_purchase(client, item["id"], quantity=10, rate=40.0, gst_percent=5.0)
    return item


def test_profit_summary_reports_sales_and_cogs(test_client):
    item = _seed_item_with_stock(test_client)
    sale_one = create_sale(test_client, item["id"], quantity=4, rate=120.0, gst_percent=5.0)
    sale_two = create_sale(test_client, item["id"], quantity=2, rate=130.0, gst_percent=5.0)

    response = test_client.get("/api/v1/analytics/profit-summary")
    assert response.status_code == 200
    data = response.json()

    expected_total_sales = sale_one["total_amount"] + sale_two["total_amount"]
    expected_cogs = sale_one["cogs"] + sale_two["cogs"]

    assert data["total_sales"] == pytest.approx(expected_total_sales)
    assert data["cogs"] == pytest.approx(expected_cogs)
    assert data["gross_profit"] == pytest.approx(expected_total_sales - expected_cogs)
    assert data["net_profit"] == pytest.approx(expected_total_sales - expected_cogs)


def test_stock_levels_flag_low_stock_items(test_client):
    item = _seed_item_with_stock(test_client, low_stock_threshold=4)
    sale = create_sale(test_client, item["id"], quantity=7, rate=100.0, gst_percent=5.0)

    response = test_client.get("/api/v1/analytics/stock-levels")
    assert response.status_code == 200
    stock_levels = response.json()

    entry = next((entry for entry in stock_levels if entry["item_id"] == item["id"]), None)
    assert entry is not None, "Expected analytics response to include the seeded item"
    assert entry["item_name"] == item["name"]
    assert entry["stock"] == sale["remaining_stock"]
    assert entry["is_low_stock"] is True
