"""
UsersLogin tests
"""
import pytest
from src.core.users.application.users_login import UsersLogin
from src.core.users.domain.errors.user_credentials_error import (
    UserCredentialsError,
)
from src.core.users.domain.user import User
from src.core.users.infrastructure.user_repository_fake import UsersRepositoryFake
from src.core.shared.services.password.plain_text_password import PlainTextPassword
from src.core.shared.services.tokenizer.jwt_tokenizer import JwtTokenizer
from src.tests.fixtures.user_fixture import JANE, JOHN

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="module")
def password_hasher():
    """
    Fixture to not compute hard passwords when registering users in use case
    """
    return PlainTextPassword()


@pytest.fixture(scope="module")
def tokenizer():
    """
    Fixture to not compute hard passwords when registering users in use case
    """
    return JwtTokenizer("secret")


def test_user_login_returns_token(password_hasher, tokenizer):
    """
    Check user is found and returns auth token successfully
    """
    existing_user = User.create(
        nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersLogin(users_repository, password_hasher, tokenizer)

    result = users_registerer.execute(JOHN["email"], JOHN["password"])

    assert result is not None


def test_user_not_found_raises_credentials_error(password_hasher, tokenizer):
    """
    Checks user not found in repository by email raises UserCredentialsError
    """
    users_repository = UsersRepositoryFake()
    users_registerer = UsersLogin(users_repository, password_hasher, tokenizer)

    with pytest.raises(UserCredentialsError):
        users_registerer.execute(JOHN["email"], JOHN["password"])


def test_user_password_not_matches_raises_credentials_error(password_hasher, tokenizer):
    """
    Checks password hasher fails if password does not match user's found in repository
    """
    existing_user = User.create(
        nickname=JANE["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersLogin(users_repository, password_hasher, tokenizer)

    with pytest.raises(UserCredentialsError):
        users_registerer.execute(JOHN["email"], JANE["password"])


# pylint: enable=redefined-outer-name
