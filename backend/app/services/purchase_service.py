from typing import List

from sqlalchemy.orm import Session

from app.db.models.purchase_batch import PurchaseBatch
from app.factories.gst_factory import get_gst_engine
from app.schemas.purchase_schema import PurchaseCreate


def _compute_total_amount(quantity: int, rate: float, gst_percent: float) -> float:
    """Return the total amount for a purchase batch including GST."""
    base_amount = quantity * rate
    gst_amount = base_amount * (gst_percent / 100)
    return base_amount + gst_amount


gst_engine = get_gst_engine()


def create_purchase_batch(db: Session, purchase_in: PurchaseCreate) -> PurchaseBatch:
    """Persist a new purchase batch and set remaining stock equal to the purchased quantity."""
    gst_percent = purchase_in.gst_percent or 0.0
    total_amount = _compute_total_amount(purchase_in.quantity, purchase_in.rate, gst_percent)
    batch = PurchaseBatch(
        item_id=purchase_in.item_id,
        quantity=purchase_in.quantity,
        remaining_qty=purchase_in.quantity,
        rate=purchase_in.rate,
        gst_percent=gst_percent,
        total_amount=total_amount,
        invoice_number=purchase_in.invoice_number,
    )
    db.add(batch)
    db.commit()
    db.refresh(batch)

    base_amount = purchase_in.quantity * purchase_in.rate
    gst_amount = base_amount * (gst_percent / 100)
    gst_engine.log_entry(db, batch.id, "purchase", gst_amount, gst_percent)

    return batch


def list_purchase_batches(db: Session, skip: int = 0, limit: int = 100) -> List[PurchaseBatch]:
    """Return a slice of stored purchase batches ordered by creation time."""
    return (
        db.query(PurchaseBatch)
        .order_by(PurchaseBatch.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
