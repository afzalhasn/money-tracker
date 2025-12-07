"""Factory for inventory engines so FIFO consumption is pluggable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Tuple

from sqlalchemy.orm import Session

from app.services.fifo_service import allocate_stock
from uuid import UUID


class InventoryEngine(Protocol):
    """Defines an interface for inventory consumption engines."""

    def allocate(
        self, db: Session, item_id: UUID, quantity: int
    ) -> Tuple[float, int]:
        """Subtract quantity from inventory and return (COGS, remaining stock)."""


@dataclass
class FifoInventoryEngine:
    """Concrete FIFO implementation wiring the FIFO service."""

    def allocate(self, db: Session, item_id: UUID, quantity: int) -> Tuple[float, int]:
        return allocate_stock(db, item_id, quantity)


def get_inventory_engine() -> InventoryEngine:
    """Return the default inventory engine implementation."""
    return FifoInventoryEngine()
