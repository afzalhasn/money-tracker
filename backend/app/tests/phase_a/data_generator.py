from typing import Dict

from fastapi.testclient import TestClient


def build_item_payload(
    name: str = "Test Widget",
    sku: str = "TW-001",
    unit: str = "pcs",
    low_stock_threshold: int = 0,
) -> Dict[str, object]:
    """Return a reusable payload for creating inventory items."""
    return {
        "name": name,
        "sku": sku,
        "unit": unit,
        "low_stock_threshold": low_stock_threshold,
    }


def build_purchase_payload(
    item_id: str,
    quantity: int = 10,
    rate: float = 100.0,
    gst_percent: float = 5.0,
    invoice_number: str = "INV-1001",
) -> Dict[str, object]:
    """Build a purchase request body for the given item."""
    return {
        "item_id": item_id,
        "quantity": quantity,
        "rate": rate,
        "gst_percent": gst_percent,
        "invoice_number": invoice_number,
    }


def build_sale_payload(
    item_id: str,
    quantity: int = 5,
    rate: float = 150.0,
    gst_percent: float = 5.0,
) -> Dict[str, object]:
    """Build a sale request body for the given item."""
    return {
        "item_id": item_id,
        "quantity": quantity,
        "rate": rate,
        "gst_percent": gst_percent,
    }


def create_item(client: TestClient, **payload_kwargs) -> Dict[str, object]:
    """Helper that creates an item and returns the API response."""
    payload = build_item_payload(**payload_kwargs)
    response = client.post("/api/v1/items/", json=payload)
    response.raise_for_status()
    return response.json()


def create_purchase(client: TestClient, item_id: str, **payload_kwargs) -> Dict[str, object]:
    """Helper that creates a purchase and returns the API response."""
    payload = build_purchase_payload(item_id=item_id, **payload_kwargs)
    response = client.post("/api/v1/purchases/", json=payload)
    response.raise_for_status()
    return response.json()


def create_sale(client: TestClient, item_id: str, **payload_kwargs) -> Dict[str, object]:
    """Helper that creates a sale and returns the API response."""
    payload = build_sale_payload(item_id=item_id, **payload_kwargs)
    response = client.post("/api/v1/sales/", json=payload)
    response.raise_for_status()
    return response.json()


def seed_phase_a_data(client: TestClient, **overrides) -> Dict[str, Dict[str, object]]:
    """
    Generate data across the Phase A APIs so tests can operate on a known state.

    Returns:
        { 'item': {...}, 'purchase': {...} }
    """
    item = create_item(client, **overrides.get("item", {}))
    purchase = create_purchase(
        client,
        item_id=item["id"],
        **overrides.get("purchase", {}),
    )
    return {"item": item, "purchase": purchase}
