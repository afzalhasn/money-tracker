from typing import List

from sqlalchemy.orm import Session

from app.db.models.item import Item
from app.schemas.item_schema import ItemCreate
import logging
logger = logging.getLogger(__name__)


def create_item(db: Session, item_in: ItemCreate) -> Item:
    """Persist a new item and return the freshly saved model."""
    db_item = Item(**item_in.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id) -> Item | None:
    """Return a single item by primary key."""
    return db.query(Item).filter(Item.id == item_id).first()


def list_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Retrieve a paginated list of items from the database.
    
    Args:
        db (Session): SQLAlchemy database session for executing queries.
        skip (int, optional): Number of items to skip from the beginning. Defaults to 0.
        limit (int, optional): Maximum number of items to return. Defaults to 100.
    
    Returns:
        List[Item]: A list of Item objects matching the query criteria.
    
    Raises:
        None
    
    Example:
        >>> items = list_items(db, skip=10, limit=50)
        >>> print(len(items))
        50
    """
    result = db.query(Item).offset(skip).limit(limit).all()
    logger.info("Listed %d items from the database", len(result))
    return result
