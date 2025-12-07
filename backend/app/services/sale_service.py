from typing import Tuple

from sqlalchemy.orm import Session

from app.db.models.item import Item
from app.db.models.sale import Sale
from app.schemas.sale_schema import SaleCreate
from app.factories.inventory_factory import get_inventory_engine
from app.factories.gst_factory import get_gst_engine

inventory_engine = get_inventory_engine()
gst_engine = get_gst_engine()


def _compute_total_amount(quantity: int, rate: float, gst_percent: float) -> float:
    """Return the total sale amount including GST."""
    base_amount = quantity * rate
    gst_amount = base_amount * (gst_percent / 100)
    return base_amount + gst_amount


def create_sale(db: Session, sale_in: SaleCreate) -> Tuple[Sale, int]:
    """Create a sale record, adjust FIFO batches, and refresh cached stock."""
    item = db.query(Item).filter(Item.id == sale_in.item_id).first()
    if not item:
        raise ValueError("Item does not exist.")

    gst_percent = sale_in.gst_percent or 0.0
    cogs, remaining_stock = inventory_engine.allocate(db, sale_in.item_id, sale_in.quantity)
    total_amount = _compute_total_amount(sale_in.quantity, sale_in.rate, gst_percent)
    item.cached_stock = remaining_stock

    sale = Sale(
        item_id=sale_in.item_id,
        quantity=sale_in.quantity,
        rate=sale_in.rate,
        gst_percent=gst_percent,
        total_amount=total_amount,
        cogs=cogs,
    )

    db.add(sale)
    db.commit()
    db.refresh(sale)

    base_amount = sale_in.quantity * sale_in.rate
    gst_amount = base_amount * (gst_percent / 100)
    gst_engine.log_entry(db, sale.id, "sale", gst_amount, gst_percent)

    return sale, remaining_stock


def list_sales(db: Session, skip: int = 0, limit: int = 100) -> list[Sale]:
    """Return the most recent sales with pagination."""
    return (
        db.query(Sale)
        .order_by(Sale.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
