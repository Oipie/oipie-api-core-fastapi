"""
ApiClient
"""
from http import HTTPStatus
from fastapi.testclient import TestClient
from src.api.routers.recipes.models.recipe_out import RecipeOut
from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.api.routers.users.models.user_login_in import UserLoginIn
from src.api.routers.users.models.user_login_out import UserLoginOut
from src.shared.models.paginated_model import PaginatedModel


class ApiClient:
    """
    Class to provide each endpoint interaction for testing purposes
    """

    def __init__(self, client: TestClient) -> None:
        self._client = client

    def get_recipes(
        self, expected_status_code=HTTPStatus.OK
    ) -> PaginatedModel[RecipeOut]:
        """
        GET /recipes endpoint
        """
        response = self._client.get("/recipes")

        assert response.status_code == expected_status_code

        return response.json()

    def create_user(
        self, user_create_dto: UserCreateDto, expected_status_code=HTTPStatus.CREATED
    ) -> None:
        """
        POST /users endpoint
        """
        response = self._client.post("/users", json=user_create_dto.dict())

        assert response.status_code == expected_status_code

    def login_user(
        self, user_login_in: UserLoginIn, expected_status_code=HTTPStatus.CREATED
    ) -> UserLoginOut:
        """
        POST /users/login endpoint
        """
        response = self._client.post("/users/login", json=user_login_in.dict())

        assert response.status_code == expected_status_code
