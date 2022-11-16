"""
Routes file for Recipes
"""
from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.api.routers.users.models.user_login_in import UserLoginIn
from src.api.routers.users.models.user_login_out import UserLoginOut
from src.api.routers.users.models.user_response_dto import UserResponseDto
from src.core.users.application.users_login import UsersLogin
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.infrastructure.dependencies import users_login, users_registerer

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=HTTPStatus.CREATED)
async def create(
    user_create_dto: UserCreateDto,
    users_registerer_use_case: UsersRegisterer = Depends(users_registerer),
):
    """
    Create a new user
    """
    created_user = users_registerer_use_case.execute(
        nickname=user_create_dto.nickname,
        email=user_create_dto.email,
        password=user_create_dto.password,
    )

    return UserResponseDto.from_domain_object(created_user)


@router.post("/login", status_code=HTTPStatus.CREATED, response_model=UserLoginOut)
async def login(
    user_login_in: UserLoginIn, users_login_use_case: UsersLogin = Depends(users_login)
):
    """
    Authenticates an existing user
    """
    auth_token = users_login_use_case.execute(
        user_login_in.email, user_login_in.password
    )

    return UserLoginOut.from_domain_object(auth_token)
