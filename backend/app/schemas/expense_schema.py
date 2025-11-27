# backend/app/schemas/expense_schema.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    note: Optional[str] = None

class ExpenseRead(BaseModel):
    id: UUID
    category: str
    amount: float
    note: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
