# backend/app/schemas/expense_schema.py
from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
