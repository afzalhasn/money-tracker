from fastapi import APIRouter

from . import items, purchases, sales

router = APIRouter()
router.include_router(items.router)
router.include_router(purchases.router)
router.include_router(sales.router)
