"""
Routes file for Recipes
"""
from fastapi import APIRouter, Depends
from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.infrastructure.dependencies import users_registerer

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def index(
    user_create_dto: UserCreateDto,
    users_registerer_use_case: UsersRegisterer = Depends(users_registerer),
):
    """
    Returns a list of recipes
    """
    users_registerer_use_case.execute(
        nickname=user_create_dto.nickname,
        email=user_create_dto.email,
        password=user_create_dto.password,
    )
