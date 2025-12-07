from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.gst_schema import GSTSummary
from app.factories.gst_factory import get_gst_engine

router = APIRouter(prefix="/gst", tags=["gst"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary", response_model=GSTSummary)
def read_gst_summary(db: Session = Depends(get_db)) -> GSTSummary:
    """Return aggregated GST totals."""
    gst_engine = get_gst_engine()
    return gst_engine.summary(db)
