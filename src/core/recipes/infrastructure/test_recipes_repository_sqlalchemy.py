"""
User repository SQLAlchemy implementation tests
"""
import pytest
from sqlalchemy.orm import Session
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.users.domain.user import User
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_model import UserModel
from src.tests.fixtures.user_fixture import JOHN

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture()
def recipes_repository(session_handler: Session) -> RecipesRepositorySQLAlchemy:
    """
    Creates a RecipesRepositorySQLAlchemy instance with session
    """

    return RecipesRepositorySQLAlchemy(session_handler)


@pytest.fixture()
def create_pancake_recipe(session_handler: Session):
    """
    Creates recipe from PANCAKE fixture
    """
    pancake_model = RecipeModel(
        uuid=JOHN["uuid"],
        nickname=JOHN["nickname"],
        email=JOHN["email"],
        password=JOHN["password"],
    )

    session_handler.add(pancake_model)
    session_handler.flush()


def test_find_by_email_not_finds_client(users_repository: UsersRepositorySQLAlchemy):
    """
    Checks user is not found if email does not exist in repository
    """
    email = JOHN["email"]

    user = users_repository.find_by_email(email)

    assert user is None


def test_find_by_email_finds_client(
    users_repository: UsersRepositorySQLAlchemy, create_john_user
):
    """
    Checks user is found if email exists in repository
    """
    email = JOHN["email"]

    user = users_repository.find_by_email(email)

    assert user is not None
    serialized_user = user.serialize()
    assert serialized_user["email"] == email


def test_find_by_nickname_not_finds_client(users_repository: UsersRepositorySQLAlchemy):
    """
    Checks user is not found if nickname does not exist in repository
    """
    nickname = JOHN["nickname"]

    user = users_repository.find_by_nickname(nickname)

    assert user is None


def test_find_by_nickname_finds_client(
    users_repository: UsersRepositorySQLAlchemy, create_john_user
):
    """
    Checks user is found if nickname exists in repository
    """
    nickname = JOHN["nickname"]

    user = users_repository.find_by_nickname(nickname)

    assert user is not None
    serialized_user = user.serialize()
    assert serialized_user["nickname"] == nickname


def test_create_creates_new_recipe(users_repository: UsersRepositorySQLAlchemy):
    """
    Checks new user creation
    """
    user = RecipeModel.create(JOHN["nickname"], JOHN["email"], JOHN["password"])

    user_created = users_repository.create(user)

    assert user_created is not None
    assert user_created.uuid is not None
    assert user_created.nickname == JOHN["nickname"]
    assert user_created.email == JOHN["email"]
    assert user_created.password == JOHN["password"]
