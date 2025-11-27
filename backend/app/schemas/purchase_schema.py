# backend/app/schemas/purchase_schema.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class PurchaseCreate(BaseModel):
    item_id: UUID
    quantity: int
    rate: float
    gst_percent: Optional[float] = 0.0
    invoice_number: Optional[str] = None

class PurchaseRead(BaseModel):
    id: UUID
    item_id: UUID
    quantity: int
    remaining_qty: int
    rate: float
    gst_percent: float
    total_amount: float
    invoice_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
