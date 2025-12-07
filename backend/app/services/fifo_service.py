from typing import Tuple

from sqlalchemy.orm import Session

from app.db.models.purchase_batch import PurchaseBatch
from uuid import UUID


def _fetch_batches(db: Session, item_id: UUID):
    return (
        db.query(PurchaseBatch)
        .filter(
            PurchaseBatch.item_id == item_id,
            PurchaseBatch.remaining_qty > 0,
        )
        .order_by(PurchaseBatch.created_at)
        .all()
    )


def allocate_stock(db: Session, item_id: UUID, quantity: int) -> Tuple[float, int]:
    batches = _fetch_batches(db, item_id)
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
        raise ValueError("Insufficient stock to fulfill the requested sale quantity.")

    remaining_stock = sum(batch.remaining_qty for batch in batches)
    return cogs, remaining_stock
