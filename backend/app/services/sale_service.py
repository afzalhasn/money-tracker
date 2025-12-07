from typing import List, Tuple

from sqlalchemy.orm import Session

from app.db.models.item import Item
from app.db.models.purchase_batch import PurchaseBatch
from app.db.models.sale import Sale
from app.schemas.sale_schema import SaleCreate


def _compute_total_amount(quantity: int, rate: float, gst_percent: float) -> float:
    """Return the total sale amount including GST."""
    base_amount = quantity * rate
    gst_amount = base_amount * (gst_percent / 100)
    return base_amount + gst_amount


def _allocate_stock(batches: List[PurchaseBatch], quantity: int) -> float:
    """Drain FIFO purchase batches to compute the COGS."""
    remaining_to_allocate = quantity
    cogs = 0.0

    for batch in batches:
        if remaining_to_allocate <= 0:
            break

        available = batch.remaining_qty
        if available <= 0:
            continue

        consume = min(available, remaining_to_allocate)
        batch.remaining_qty -= consume
        remaining_to_allocate -= consume
        cogs += consume * batch.rate

    if remaining_to_allocate > 0:
        raise ValueError(
            "Insufficient stock to fulfill the requested sale quantity."
        )

    return cogs


def create_sale(db: Session, sale_in: SaleCreate) -> Tuple[Sale, int]:
    """
    Create a sale record, adjust the FIFO batches, and update cached stock.

    Returns:
        Tuple[Sale, int]: the saved Sale and the remaining stock for the item.
    """
    item = db.query(Item).filter(Item.id == sale_in.item_id).first()
    if not item:
        raise ValueError("Item does not exist.")

    batches = (
        db.query(PurchaseBatch)
        .filter(
            PurchaseBatch.item_id == sale_in.item_id,
            PurchaseBatch.remaining_qty > 0,
        )
        .order_by(PurchaseBatch.created_at)
        .all()
    )

    total_available = sum(batch.remaining_qty for batch in batches)
    if total_available < sale_in.quantity:
        raise ValueError(
            f"Insufficient stock for item {sale_in.item_id}. "
            f"Available {total_available}, requested {sale_in.quantity}."
        )

    gst_percent = sale_in.gst_percent or 0.0
    cogs = _allocate_stock(batches, sale_in.quantity)
    total_amount = _compute_total_amount(sale_in.quantity, sale_in.rate, gst_percent)
    remaining_stock = sum(batch.remaining_qty for batch in batches)
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

    return sale, remaining_stock


def list_sales(db: Session, skip: int = 0, limit: int = 100) -> List[Sale]:
    """Return the most recent sales with pagination."""
    return (
        db.query(Sale)
        .order_by(Sale.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
