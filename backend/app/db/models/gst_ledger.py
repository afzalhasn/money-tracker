# backend/app/db/models/gst_ledger.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class GSTLedger(Base):
    __tablename__ = "gst_ledger"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    reference_id = Column(UUID(as_uuid=True), nullable=True)  # purchase or sale id
    reference_type = Column(String(32), nullable=True)  # 'purchase' or 'sale'
    gst_amount = Column(Float, nullable=False)
    gst_percent = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_by = relationship("User")
