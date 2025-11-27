# backend/app/db/models/item.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    sku = Column(String(100), nullable=True, index=True)
    unit = Column(String(50), nullable=True)  # e.g., kg, pcs
    low_stock_threshold = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # current stock is computed from batches, but keep optional cached field
    cached_stock = Column(Integer, default=0)

    purchase_batches = relationship("PurchaseBatch", back_populates="item")
    sales = relationship("Sale", back_populates="item")
