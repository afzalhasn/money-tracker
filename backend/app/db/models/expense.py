# backend/app/db/models/expense.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    category = Column(String(128), nullable=False)
    amount = Column(Float, nullable=False)
    note = Column(String(1024), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_by = relationship("User", back_populates="expenses")
