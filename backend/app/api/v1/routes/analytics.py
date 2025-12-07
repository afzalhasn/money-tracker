from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.analytics_schema import ProfitSummary, StockLevel
from app.services.profit_service import get_profit_summary, get_stock_levels

router = APIRouter(prefix="/analytics", tags=["analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/profit-summary", response_model=ProfitSummary)
def read_profit_summary(db: Session = Depends(get_db)) -> ProfitSummary:
    """Return aggregated profit metrics."""
    return get_profit_summary(db)


@router.get("/stock-levels", response_model=List[StockLevel])
def read_stock_levels(db: Session = Depends(get_db)) -> List[StockLevel]:
    """Return stock level summaries for each item."""
    return get_stock_levels(db)
