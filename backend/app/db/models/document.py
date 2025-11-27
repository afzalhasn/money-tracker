# backend/app/db/models/document.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    filename = Column(String(512), nullable=False)
    filepath = Column(String(1024), nullable=False)
    file_type = Column(String(64), nullable=True)
    transaction_id = Column(UUID(as_uuid=True), nullable=True)  # could point to sale or purchase by id
    transaction_type = Column(String(32), nullable=True)  # 'purchase' | 'sale' | etc.
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    uploaded_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    uploaded_by = relationship("User")
