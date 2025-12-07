import pytest

from app.tests.phase_a.data_generator import create_item, create_purchase, create_sale


def test_fifo_consumes_oldest_batches_before_newer(test_client):
    """Sales should consume FIFO batches for COGS and remaining stock tracking."""
    item = create_item(test_client, name="FIFO Widget", sku="FIFO-001")
    # Create two batches: older batch with lower rate should be consumed first.
    create_purchase(test_client, item["id"], quantity=5, rate=50.0, gst_percent=5.0)
    create_purchase(test_client, item["id"], quantity=10, rate=60.0, gst_percent=5.0)

    sale = create_sale(
        test_client,
        item["id"],
        quantity=8,
        rate=120.0,
        gst_percent=5.0,
    )

    assert sale["remaining_stock"] == 7
    assert sale["cogs"] == pytest.approx(250.0 + 180.0)
