import pytest

from .data_generator import (
    build_sale_payload,
    create_sale,
    seed_phase_a_data,
)


def _expected_total(quantity: int, rate: float, gst_percent: float) -> float:
    """Compute the expected total amount for comparison."""
    base = quantity * rate
    return base + base * (gst_percent / 100)


def test_create_sale_consumes_fifo_stock(test_client):
    """Sales API should drain purchase batches, compute COGS, and expose remaining stock."""
    data = seed_phase_a_data(
        test_client,
        purchase={"quantity": 12, "rate": 60.0},
    )

    sale_response = create_sale(
        test_client,
        data["item"]["id"],
        quantity=5,
        rate=100.0,
        gst_percent=5.0,
    )

    assert sale_response["remaining_stock"] == 7
    assert sale_response["cogs"] == 5 * data["purchase"]["rate"]
    assert sale_response["total_amount"] == pytest.approx(
        _expected_total(5, 100.0, 5.0), rel=1e-3
    )


def test_read_sales_returns_history(test_client):
    """Sales listing should return the previously recorded entries."""
    data = seed_phase_a_data(
        test_client,
        purchase={"quantity": 8, "rate": 50.0},
    )
    sale_response = create_sale(
        test_client,
        data["item"]["id"],
        quantity=3,
        rate=120.0,
        gst_percent=5.0,
    )

    list_response = test_client.get("/api/v1/sales/")
    assert list_response.status_code == 200
    ids = {entry["id"] for entry in list_response.json()}
    assert sale_response["id"] in ids


def test_sale_rejected_when_stock_insufficient(test_client):
    """Attempting to sell more than available inventory should return 400."""
    data = seed_phase_a_data(
        test_client,
        purchase={"quantity": 3},
    )

    payload = build_sale_payload(
        item_id=data["item"]["id"],
        quantity=10,
        rate=120.0,
        gst_percent=5.0,
    )
    response = test_client.post("/api/v1/sales/", json=payload)

    assert response.status_code == 400
    assert "Insufficient stock" in response.json()["detail"]
