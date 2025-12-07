from fastapi import APIRouter

from . import analytics, items, purchases, sales, gst

router = APIRouter()
router.include_router(items.router)
router.include_router(purchases.router)
router.include_router(sales.router)
router.include_router(gst.router)
router.include_router(analytics.router)
