from fastapi import APIRouter

from . import items, purchases

router = APIRouter()
router.include_router(items.router)
router.include_router(purchases.router)
