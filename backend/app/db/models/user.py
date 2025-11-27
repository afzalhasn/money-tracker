# backend/app/db/models/user.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
import enum

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String(150), unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    full_name = Column(String(255), nullable=True)
    role = Column(Enum(UserRole), default=UserRole.STAFF, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    purchases = relationship("PurchaseBatch", back_populates="created_by")
    sales = relationship("Sale", back_populates="created_by")
    expenses = relationship("Expense", back_populates="created_by")
    investments = relationship("Investment", back_populates="created_by")
