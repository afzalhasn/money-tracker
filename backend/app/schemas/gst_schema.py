# backend/app/schemas/gst_schema.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class GSTEntryCreate(BaseModel):
    reference_id: UUID
    reference_type: str  # 'purchase' or 'sale'
    gst_amount: float
    gst_percent: float

class GSTEntryRead(BaseModel):
    id: UUID
    reference_id: UUID
    reference_type: str
    gst_amount: float
    gst_percent: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class GSTSummary(BaseModel):
    gst_input: float
    gst_output: float
    difference: float
