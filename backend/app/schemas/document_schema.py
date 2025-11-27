# backend/app/schemas/document_schema.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class DocumentUpload(BaseModel):
    transaction_id: Optional[UUID]
    transaction_type: Optional[str]  # 'purchase' | 'sale'
    file_type: Optional[str] = None

class DocumentRead(BaseModel):
    id: UUID
    filename: str
    filepath: str
    file_type: Optional[str]
    transaction_id: Optional[UUID]
    transaction_type: Optional[str]
    uploaded_at: datetime

    class Config:
        orm_mode = True
