from .data_generator import create_item, create_purchase


def test_create_purchase_records_stock(test_client):
    """Purchases API should persist a batch with the requested quantities."""
    item = create_item(test_client, name="Purchase Widget", sku="PW-001")
    purchase = create_purchase(test_client, item["id"], quantity=12, rate=90.0)

    assert purchase["item_id"] == item["id"]
    assert purchase["quantity"] == 12
    assert purchase["remaining_qty"] == 12
    assert purchase["rate"] == 90.0


def test_read_purchases_returns_created_batches(test_client):
    """Purchases should be listed through the GET endpoint."""
    item = create_item(test_client, name="List Purchase", sku="LP-001")
    create_purchase(test_client, item["id"], quantity=5, rate=80.0)

    response = test_client.get("/api/v1/purchases/")
    assert response.status_code == 200
    assert any(batch["item_id"] == item["id"] for batch in response.json())
