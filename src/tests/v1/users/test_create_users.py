"""
E2E tests for user creation
"""

from http import HTTPStatus
from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.tests.fixtures.user_fixture import JANE, JOHN
from src.tests.utils.api_client import ApiClient


def test_create_user(api_client: ApiClient):
    """
    This test creates a user and checks that the response is the expected one
    """

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )


def test_create_user_fails_with_repeated_nickname(api_client: ApiClient):
    """
    This test fails if the user is created with a repeated nickname
    """

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JANE["email"], password=JANE["password"]
        ),
        expected_status_code=HTTPStatus.CONFLICT,
    )


def test_create_user_fails_with_repeated_email(api_client: ApiClient):
    """
    This test fails if the user is created with a repeated email
    """

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )

    api_client.create_user(
        UserCreateDto(
            nickname=JANE["nickname"], email=JOHN["email"], password=JANE["password"]
        ),
        expected_status_code=HTTPStatus.CONFLICT,
    )


def test_create_multiple_users(api_client: ApiClient):
    """
    This test creates two users and checks that the response is the expected one
    """

    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )
    api_client.create_user(
        UserCreateDto(
            nickname=JANE["nickname"], email=JANE["email"], password=JANE["password"]
        ),
    )
