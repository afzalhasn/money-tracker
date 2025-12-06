from typing import List

from sqlalchemy.orm import Session

from app.db.models.item import Item
from app.schemas.item_schema import ItemCreate
import logging
logger = logging.getLogger(__name__)


def create_item(db: Session, item_in: ItemCreate) -> Item:
    """Persist a new item and return the freshly saved model."""
    db_item = Item(**item_in.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id) -> Item | None:
    """Return a single item by primary key."""
    return db.query(Item).filter(Item.id == item_id).first()


def list_items(db: Session, skip: int = 0, limit: int = 100):
    # Query the database, then log and return the paginated records.
    result = db.query(Item).offset(skip).limit(limit).all()
    logger.info("Listed %d items from the database", len(result))
    return result
