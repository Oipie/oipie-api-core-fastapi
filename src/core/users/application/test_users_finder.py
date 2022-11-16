"""
UsersLogin tests
"""
import pytest

from src.core.users.application.users_finder import UsersFinder
from src.core.users.domain.errors.user_not_found_error import UserNotFoundError
from src.core.users.domain.user import User
from src.core.users.infrastructure.user_repository_fake import UsersRepositoryFake
from src.tests.fixtures.user_fixture import JOHN

# pylint: disable=redefined-outer-name


def test_user_login_returns_token():
    """
    Check user is found
    """
    existing_user = User.create(
        nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_finder = UsersFinder(users_repository)

    result = users_finder.execute(JOHN["email"])

    assert result is not None
    assert result.email == JOHN["email"]


def test_user_not_found_raises_credentials_error():
    """
    Checks user not found in repository by email raises UserNotFoundError
    """
    users_repository = UsersRepositoryFake()
    users_registerer = UsersFinder(users_repository)

    with pytest.raises(UserNotFoundError):
        users_registerer.execute(JOHN["email"])


# pylint: enable=redefined-outer-name
