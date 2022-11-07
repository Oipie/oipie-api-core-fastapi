"""
UsersRegisterer tests
"""
import pytest
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.domain.errors.user_with_email_already_exists_error import (
    UserWithEmailAlreadyExistsError,
)
from src.core.users.domain.errors.user_with_nickname_already_exists_error import (
    UserWithNicknameAlreadyExistsError,
)
from src.core.users.domain.user import User
from src.core.users.infrastructure.user_repository_fake import UsersRepositoryFake
from src.core.shared.services.password.plain_text_password import PlainTextPassword
from src.tests.fixtures.user_fixture import JANE, JOHN

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="module")
def password_hasher():
    """
    Fixture to not compute hard passwords when registering users in use case
    """
    return PlainTextPassword()


def test_new_user_is_registered(password_hasher):
    """
    Checks user is successfully registered by not raising an error
    """
    users_repository = UsersRepositoryFake()
    users_registerer = UsersRegisterer(users_repository, password_hasher)

    users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])


def test_registerer_raises_user_with_email_error(password_hasher):
    """
    Checks user is successfully registered by not raising an error
    """
    existing_user = User.create(
        nickname=JANE["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersRegisterer(users_repository, password_hasher)

    with pytest.raises(UserWithEmailAlreadyExistsError):
        users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])


def test_registerer_raises_user_with_nickname_error(password_hasher):
    """
    Checks user is successfully registered by not raising an error
    """
    existing_user = User.create(
        nickname=JOHN["nickname"], email=JANE["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersRegisterer(users_repository, password_hasher)

    with pytest.raises(UserWithNicknameAlreadyExistsError):
        users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])


# pylint: enable=redefined-outer-name
