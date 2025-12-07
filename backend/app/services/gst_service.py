from typing import Literal

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models.gst_ledger import GSTLedger
from app.schemas.gst_schema import GSTSummary

ReferenceType = Literal["purchase", "sale"]


def record_gst_entry(
    db: Session,
    reference_id,
    reference_type: ReferenceType,
    gst_amount: float,
    gst_percent: float,
) -> GSTLedger:
    """Persist a GST ledger entry for the provided reference."""
    entry = GSTLedger(
        reference_id=reference_id,
        reference_type=reference_type,
        gst_amount=gst_amount,
        gst_percent=gst_percent,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_gst_summary(db: Session) -> GSTSummary:
    """Sum up all GST postings to compute input/output/difference."""
    gst_input = (
        db.query(func.coalesce(func.sum(GSTLedger.gst_amount), 0.0))
        .filter(GSTLedger.reference_type == "purchase")
        .scalar()
        or 0.0
    )
    gst_output = (
        db.query(func.coalesce(func.sum(GSTLedger.gst_amount), 0.0))
        .filter(GSTLedger.reference_type == "sale")
        .scalar()
        or 0.0
    )
    return GSTSummary(
        gst_input=gst_input,
        gst_output=gst_output,
        difference=gst_input - gst_output,
    )
