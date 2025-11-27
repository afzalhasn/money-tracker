# backend/app/schemas/investment_schema.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class InvestmentCreate(BaseModel):
    investor_name: str
    amount: float
    note: Optional[str] = None

class InvestmentRead(BaseModel):
    id: UUID
    investor_name: str
    amount: float
    note: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
