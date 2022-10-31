"""
App definition
"""

import databases
from fastapi import FastAPI
from src.config.database import database_url_connection
from src.api.routers.recipes import recipes
from src.api.routers.health import health

DATABASE_URL = database_url_connection()

database = databases.Database(DATABASE_URL)

app = FastAPI()
app.include_router(recipes.router)
app.include_router(health.router)
