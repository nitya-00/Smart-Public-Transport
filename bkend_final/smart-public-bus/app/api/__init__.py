from fastapi import APIRouter

router = APIRouter()

from .routers import buses, health

router.include_router(buses.router, prefix="/buses", tags=["buses"])
router.include_router(health.router, prefix="/health", tags=["health"])