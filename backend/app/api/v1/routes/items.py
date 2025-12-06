from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.item_schema import ItemCreate, ItemRead
from app.services.item_service import create_item, get_item, list_items

router = APIRouter(prefix="/items", tags=["items"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item_endpoint(item_in: ItemCreate, db: Session = Depends(get_db)):
    """Create and persist a new item."""
    return create_item(db, item_in)


@router.get("/", response_model=List[ItemRead])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List items with pagination."""
    return list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id: UUID, db: Session = Depends(get_db)):
    """Fetch a single item by UUID."""
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
