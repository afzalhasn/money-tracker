# backend/app/schemas/sale_schema.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class SaleCreate(BaseModel):
    item_id: UUID
    quantity: int
    rate: float
    gst_percent: Optional[float] = 0.0

class SaleRead(BaseModel):
    id: UUID
    item_id: UUID
    quantity: int
    rate: float
    gst_percent: float
    total_amount: float
    cogs: Optional[float]
    remaining_stock: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
