from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.purchase_schema import PurchaseCreate, PurchaseRead
from app.services.purchase_service import create_purchase_batch, list_purchase_batches

router = APIRouter(prefix="/purchases", tags=["purchases"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PurchaseRead, status_code=status.HTTP_201_CREATED)
def create_purchase(purchase_in: PurchaseCreate, db: Session = Depends(get_db)):
    """Record a new purchase batch."""
    return create_purchase_batch(db, purchase_in)


@router.get("/", response_model=List[PurchaseRead])
def read_purchases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List purchase batches with pagination."""
    return list_purchase_batches(db, skip=skip, limit=limit)
