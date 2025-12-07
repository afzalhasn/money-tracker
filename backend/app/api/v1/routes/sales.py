from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.sale_schema import SaleCreate, SaleRead
from app.services.sale_service import create_sale, list_sales

router = APIRouter(prefix="/sales", tags=["sales"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SaleRead, status_code=status.HTTP_201_CREATED)
def create_sale_endpoint(sale_in: SaleCreate, db: Session = Depends(get_db)):
    """Record a sale while honoring FIFO batch stock levels."""
    try:
        sale, remaining_stock = create_sale(db, sale_in)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    return {
        "id": sale.id,
        "item_id": sale.item_id,
        "quantity": sale.quantity,
        "rate": sale.rate,
        "gst_percent": sale.gst_percent,
        "total_amount": sale.total_amount,
        "cogs": sale.cogs,
        "created_at": sale.created_at,
        "remaining_stock": remaining_stock,
    }


@router.get("/", response_model=List[SaleRead])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List historical sales entries with pagination."""
    return list_sales(db, skip=skip, limit=limit)
