from .data_generator import build_item_payload, create_item


def test_create_item_and_retrieve(test_client):
    """Items API should create a record and allow fetching it by UUID."""
    payload = build_item_payload(name="Widget Alpha", sku="WA-001")
    item_response = create_item(test_client, **payload)

    assert item_response["name"] == "Widget Alpha"
    assert item_response["sku"] == "WA-001"
    assert item_response["cached_stock"] == 0

    retrieve_response = test_client.get(f"/api/v1/items/{item_response['id']}")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json()["name"] == "Widget Alpha"


def test_list_items_returns_created_rows(test_client):
    """Listing items should include all previously created entries."""
    create_item(test_client, name="Widget Beta", sku="WB-001")
    create_item(test_client, name="Widget Gamma", sku="WG-001")

    list_response = test_client.get("/api/v1/items/")
    assert list_response.status_code == 200
    names = {entry["name"] for entry in list_response.json()}
    assert "Widget Beta" in names
    assert "Widget Gamma" in names


def test_get_item_not_found_returns_404(test_client):
    """Requesting a missing item returns HTTP 404."""
    missing_uuid = "00000000-0000-0000-0000-000000000000"
    response = test_client.get(f"/api/v1/items/{missing_uuid}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
