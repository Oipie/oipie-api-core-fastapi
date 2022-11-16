"""
Routes file for Recipes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies.database import get_database

router = APIRouter(tags=["health"])


@router.get("/health")
async def show(session: Session = Depends(get_database)):
    """
    Returns 200 OK if service is alive
    """
    session.execute("SELECT 1")

    return {"status": "OK"}
