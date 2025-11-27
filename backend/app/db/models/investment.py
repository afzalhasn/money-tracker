# backend/app/db/models/investment.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class Investment(Base):
    __tablename__ = "investments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    investor_name = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    note = Column(String(1024), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_by = relationship("User", back_populates="investments")
