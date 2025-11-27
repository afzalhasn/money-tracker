# backend/app/db/models/purchase_batch.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class PurchaseBatch(Base):
    __tablename__ = "purchase_batches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    remaining_qty = Column(Integer, nullable=False)  # remaining for FIFO
    rate = Column(Float, nullable=False)  # unit cost
    gst_percent = Column(Float, nullable=True, default=0.0)
    total_amount = Column(Float, nullable=False)  # quantity * rate + gst
    invoice_number = Column(String(128), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    item = relationship("Item", back_populates="purchase_batches")
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_by = relationship("User", back_populates="purchases")
