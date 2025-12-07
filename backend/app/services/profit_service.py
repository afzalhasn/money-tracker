from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models.expense import Expense
from app.db.models.item import Item
from app.db.models.purchase_batch import PurchaseBatch
from app.db.models.sale import Sale
from app.schemas.analytics_schema import ProfitSummary, StockLevel


def get_profit_summary(db: Session) -> ProfitSummary:
    """Return aggregated profit metrics."""
    total_sales = (
        db.query(func.coalesce(func.sum(Sale.total_amount), 0.0)).scalar() or 0.0
    )
    total_cogs = db.query(func.coalesce(func.sum(Sale.cogs), 0.0)).scalar() or 0.0
    total_expenses = (
        db.query(func.coalesce(func.sum(Expense.amount), 0.0)).scalar() or 0.0
    )

    gross_profit = total_sales - total_cogs
    net_profit = gross_profit - total_expenses

    return ProfitSummary(
        total_sales=total_sales,
        cogs=total_cogs,
        gross_profit=gross_profit,
        net_profit=net_profit,
    )


def get_stock_levels(db: Session) -> List[StockLevel]:
    """Return per-item stock summaries derived from purchase batches."""
    stock_levels: List[StockLevel] = []

    items = db.query(Item).all()
    for item in items:
        remaining = (
            db.query(func.coalesce(func.sum(PurchaseBatch.remaining_qty), 0))
            .filter(PurchaseBatch.item_id == item.id)
            .scalar()
            or 0
        )
        stock_levels.append(
            StockLevel(
                item_id=str(item.id),
                item_name=item.name,
                stock=int(remaining),
                low_stock_threshold=item.low_stock_threshold or 0,
                is_low_stock=remaining <= (item.low_stock_threshold or 0),
            )
        )

    return stock_levels
