"""
API Routes
"""
from fastapi import APIRouter
from app.api.routes import databases

api_router = APIRouter()

api_router.include_router(databases.router, prefix="/databases", tags=["databases"])
