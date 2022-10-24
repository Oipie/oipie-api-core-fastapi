"""
App definition
"""

import sqlalchemy
import databases
from fastapi import FastAPI
from src.config.database import database_url_connection

DATABASE_URL = database_url_connection()

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

app = FastAPI()


@app.on_event("startup")
async def startup():
    """
    Method executed when API is started
    """
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """
    Method executed when API is shutdown
    """
    await database.disconnect()


@app.get("/health")
async def health():
    """
    Returns 200 OK if service is alive
    """
    return {"status": "OK"}
