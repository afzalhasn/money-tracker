# backend/app/schemas/item_schema.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    sku: Optional[str] = None
    unit: Optional[str] = None
    low_stock_threshold: Optional[int] = 0

class ItemRead(BaseModel):
    id: UUID
    name: str
    sku: Optional[str]
    unit: Optional[str]
    low_stock_threshold: int
    cached_stock: int
    created_at: datetime

    class Config:
        orm_mode = True
