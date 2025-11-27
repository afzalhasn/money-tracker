# backend/app/schemas/analytics_schema.py
from pydantic import BaseModel

class ProfitSummary(BaseModel):
    total_sales: float
    cogs: float
    gross_profit: float
    net_profit: float

class StockLevel(BaseModel):
    item_id: str
    item_name: str
    stock: int
    low_stock_threshold: int
    is_low_stock: bool = False
