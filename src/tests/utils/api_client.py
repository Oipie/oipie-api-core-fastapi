"""
ApiClient
"""
from http import HTTPStatus
from typing import Optional, Type

from fastapi.testclient import TestClient

from src.api.routers.recipes.models.recipe_create_dto import RecipeCreateDto
from src.api.routers.recipes.models.recipe_response_dto import RecipeResponseDto
from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.api.routers.users.models.user_login_in import UserLoginIn
from src.api.routers.users.models.user_login_out import UserLoginOut
from src.api.routers.users.models.user_response_dto import UserResponseDto
from src.shared.models.paginated_model import PaginatedModel


class ApiClient:
    """
    Class to provide each endpoint interaction for testing purposes
    """

    def __init__(self, client: TestClient) -> None:
        self._client = client

    def get_recipes(
        self, expected_status_code=HTTPStatus.OK
    ) -> PaginatedModel[RecipeResponseDto]:
        """
        GET /recipes endpoint
        """
        response = self._client.get("/recipes")

        assert response.status_code == expected_status_code

        return response.json()

    def create_recipe(
        self,
        recipe_create_dto: RecipeCreateDto,
        expected_status_code=HTTPStatus.CREATED,
    ) -> RecipeResponseDto:
        """
        POST /recipes endpoint
        """
        response = self._client.post("/recipes", json=recipe_create_dto.dict())

        assert response.status_code == expected_status_code

        return response.json()

    def create_user(
        self, user_create_dto: UserCreateDto, expected_status_code=HTTPStatus.CREATED
    ) -> UserResponseDto:
        """
        POST /users endpoint
        """

        response = self._client.post("/users/register", json=user_create_dto.dict())

        assert response.status_code == expected_status_code

        return response.json()

    def login_user(
        self, user_login_in: UserLoginIn, expected_status_code=HTTPStatus.CREATED
    ) -> UserLoginOut:
        """
        POST /users/login endpoint
        """
        response = self._client.post("/users/login", json=user_login_in.dict())

        assert response.status_code == expected_status_code

        return response.json()

    def get_me(
        self, bearer_token: Optional[str], expected_status_code=HTTPStatus.OK
    ) -> UserResponseDto:
        """
        GET /users/me endpoint
        """

        headers = {}
        if bearer_token is not None:
            headers["Authorization"] = f"Bearer {bearer_token}"

        response = self._client.get("/users/me", headers=headers)

        assert response.status_code == expected_status_code

        return response.json()
