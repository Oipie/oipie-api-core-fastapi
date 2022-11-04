"""
Routes file for Recipes
"""
from http import HTTPStatus
from fastapi import APIRouter, Depends
from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.infrastructure.dependencies import users_registerer

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=HTTPStatus.CREATED)
async def index(
    user_create_dto: UserCreateDto,
    users_registerer_use_case: UsersRegisterer = Depends(users_registerer),
):
    """
    Create a new user
    """
    users_registerer_use_case.execute(
        nickname=user_create_dto.nickname,
        email=user_create_dto.email,
        password=user_create_dto.password,
    )
