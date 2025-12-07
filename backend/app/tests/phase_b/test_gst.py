import pytest

from app.tests.phase_a.data_generator import create_item, create_purchase, create_sale


def test_gst_summary_reflects_purchase_and_sale_entries(test_client):
    """GST summary should report aggregated input/output entries recorded during purchases and sales."""
    item = create_item(test_client, name="Taxed Goods", sku="GST-001")
    create_purchase(
        test_client,
        item["id"],
        quantity=6,
        rate=200.0,
        gst_percent=12.0,
        invoice_number="GST-INV-100",
    )
    sale = create_sale(
        test_client,
        item["id"],
        quantity=2,
        rate=250.0,
        gst_percent=12.0,
    )

    purchase_gst = 6 * 200.0 * 0.12
    sale_gst = 2 * 250.0 * 0.12

    response = test_client.get("/api/v1/gst/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["gst_input"] == pytest.approx(purchase_gst)
    assert data["gst_output"] == pytest.approx(sale_gst)
    assert data["difference"] == pytest.approx(purchase_gst - sale_gst)
