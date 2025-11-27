# backend/app/db/models/sale.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    rate = Column(Float, nullable=False)  # selling price per unit
    gst_percent = Column(Float, nullable=True, default=0.0)
    total_amount = Column(Float, nullable=False)  # quantity * rate + gst
    cogs = Column(Float, nullable=True)  # computed COGS at time of sale
    created_at = Column(DateTime, default=datetime.utcnow)

    item = relationship("Item", back_populates="sales")
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_by = relationship("User", back_populates="sales")
