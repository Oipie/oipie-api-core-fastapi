"""
App definition
"""

import databases
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from src.config.database import database_url_connection
from src.api.routers.health import health
from src.api.routers.recipes import recipes
from src.api.routers.users import users
from src.core.shared.domain.base_exception import DomainException
from src.core.shared.infrastructure.domain_exception_category_http_mapper import (
    get_http_status_code_by_domain_category,
)

DATABASE_URL = database_url_connection()

database = databases.Database(DATABASE_URL)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc):
    """
    Handles validation errors on DTOs
    """

    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(DomainException)
async def domain_exception_handler(_, exc: DomainException):
    """
    Exception handler for domain exceptions
    """

    return JSONResponse(
        str(exc), status_code=get_http_status_code_by_domain_category(exc.category)
    )


app.include_router(health.router)
app.include_router(recipes.router)
app.include_router(users.router)
