"""
E2E tests for user login
"""
# pylint: disable=redefined-outer-name, unused-argument

from http import HTTPStatus

import pytest

from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.api.routers.users.models.user_login_in import UserLoginIn
from src.core.shared.services.tokenizer.jwt_tokenizer import JwtTokenizer
from src.core.shared.services.tokenizer.tokenizer import Tokenizer
from src.tests.fixtures.user_fixture import JANE, JOHN
from src.tests.utils.api_client import ApiClient


@pytest.fixture(autouse=True, scope="function")
def create_user(api_client: ApiClient):
    """
    Creates user from fixture
    """

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )


@pytest.fixture(scope="module")
def tokenizer() -> Tokenizer:
    """
    Fixture to not compute hard passwords when registering users in use case
    """

    return JwtTokenizer("secret")


@pytest.fixture
def create_john_bearer(tokenizer: Tokenizer) -> str:
    """
    Creates a valid bearer for john
    """
    return tokenizer.encode(
        {
            "email": JOHN["email"],
            "nickname": JOHN["nickname"],
        }
    )


@pytest.fixture
def create_jane_bearer(tokenizer: Tokenizer) -> str:
    """
    Creates a valid bearer for john
    """
    return tokenizer.encode(
        {
            "email": JANE["email"],
            "nickname": JANE["nickname"],
        }
    )


def test_get_user_ok(api_client: ApiClient, create_john_bearer: str):
    """
    Checks /users/me returns a 200 jwt is valid are correct
    """

    api_client.get_me(bearer_token=create_john_bearer)


def test_get_user_fails_with_wrong_email(
    api_client: ApiClient, create_jane_bearer: str
):
    """
    Checks /users/me returns a 404 if email on jwt is not valid
    """
    api_client.get_me(
        bearer_token=create_jane_bearer,
        expected_status_code=HTTPStatus.NOT_FOUND,
    )


def test_get_user_fails_without_jwt(api_client: ApiClient):
    """
    Checks /users/me returns a 404 if email on jwt is not valid
    """
    api_client.get_me(
        bearer_token="",
        expected_status_code=HTTPStatus.FORBIDDEN,
    )
