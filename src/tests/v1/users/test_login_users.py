"""
E2E tests for user login
"""
# pylint: disable=redefined-outer-name, unused-argument

from http import HTTPStatus

import pytest

from src.api.routers.users.models.user_create_dto import UserCreateDto
from src.api.routers.users.models.user_login_in import UserLoginIn
from src.tests.fixtures.user_fixture import JANE, JOHN
from src.tests.utils.api_client import ApiClient


@pytest.fixture()
def create_user(api_client: ApiClient):
    """
    Creates user from fixture
    """
    api_client.create_user(
        UserCreateDto(
            nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
        )
    )


def test_login_user_ok(api_client: ApiClient, create_user):
    """
    Checks /users/login returns a 201 with auth token if credentials are correct
    """
    api_client.login_user(UserLoginIn(email=JOHN["email"], password=JOHN["password"]))


def test_login_user_fails_with_wrong_password(api_client: ApiClient, create_user):
    """
    Checks /users/login returns a 401 if password is wrong
    """
    api_client.login_user(
        UserLoginIn(email=JOHN["email"], password=JANE["password"]),
        expected_status_code=HTTPStatus.UNAUTHORIZED,
    )


def test_login_user_fails_with_wrong_email(api_client: ApiClient, create_user):
    """
    Checks /users/login returns a 401 if password is wrong
    """
    api_client.login_user(
        UserLoginIn(email=JANE["email"], password=JOHN["password"]),
        expected_status_code=HTTPStatus.UNAUTHORIZED,
    )
