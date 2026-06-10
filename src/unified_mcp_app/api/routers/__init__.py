from fastapi import APIRouter
from .calculator import router as calculator_router
from .feed import router as feed_router

api_router = APIRouter()
api_router.include_router(calculator_router)
api_router.include_router(feed_router)
