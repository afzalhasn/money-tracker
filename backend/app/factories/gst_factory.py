"""Factory for GST engines so the GST service can be swapped later."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from sqlalchemy.orm import Session

from app.schemas.gst_schema import GSTSummary
from app.services import gst_service


class GSTEngine(Protocol):
    """Abstraction over a GST ledger implementation."""

    def log_entry(
        self,
        db: Session,
        reference_id,
        reference_type: str,
        gst_amount: float,
        gst_percent: float,
    ) -> None:
        """Record a GST ledger entry for a reference."""

    def summary(self, db: Session) -> GSTSummary:
        """Return aggregated GST totals."""


@dataclass
class DefaultGSTEngine:
    """Default GST engine delegating to gst_service."""

    def log_entry(
        self,
        db: Session,
        reference_id,
        reference_type: str,
        gst_amount: float,
        gst_percent: float,
    ) -> None:
        gst_service.record_gst_entry(db, reference_id, reference_type, gst_amount, gst_percent)

    def summary(self, db: Session) -> GSTSummary:
        return gst_service.get_gst_summary(db)


def get_gst_engine() -> GSTEngine:
    """Return the default GST engine."""
    return DefaultGSTEngine()
