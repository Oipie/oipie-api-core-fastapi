"""
User repository SQLAlchemy implementation tests
"""
import pytest
from sqlalchemy.orm import Session
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_model import UserModel
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
from src.tests.fixtures.user_fixture import JOHN

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture
def create_john_user(session_handler: Session) -> UserModel:
    """
    Creates user from JOHN fixture
    """
    john_model = UserModel(
        uuid=JOHN["uuid"],
        nickname=JOHN["nickname"],
        email=JOHN["email"],
        password=JOHN["password"],
    )

    session_handler.add(john_model)
    session_handler.flush()

    return john_model


@pytest.fixture
def pancake_recipe_model(create_john_user: UserModel) -> RecipeModel:
    """
    Return a recipe model for PANCAKE fixture
    """

    return RecipeModel(
        uuid=PANCAKE["uuid"],
        name=PANCAKE["name"],
        favourite_amount=PANCAKE["favourite_amount"],
        preparation_time=PANCAKE["preparation_time"],
        cover=PANCAKE["cover"],
        owner_id=create_john_user.uuid,
    )


@pytest.fixture
def strawberry_smoothie_recipe_model(create_john_user: UserModel) -> RecipeModel:
    """
    Return a recipe model for PANCAKE fixture
    """

    return RecipeModel(
        uuid=STRAWBERRY_SMOOTHIE["uuid"],
        name=STRAWBERRY_SMOOTHIE["name"],
        favourite_amount=STRAWBERRY_SMOOTHIE["favourite_amount"],
        preparation_time=STRAWBERRY_SMOOTHIE["preparation_time"],
        cover=STRAWBERRY_SMOOTHIE["cover"],
        owner_id=create_john_user.uuid,
    )


@pytest.fixture
def create_pancake_recipe(
    session_handler: Session, pancake_recipe_model: RecipeModel
) -> RecipeModel:
    """
    Creates recipe from PANCAKE fixture
    """

    session_handler.add(pancake_recipe_model)
    session_handler.flush()

    return pancake_recipe_model


@pytest.fixture
def create_strawberry_smoothie_recipe(
    session_handler: Session, strawberry_smoothie_recipe_model: RecipeModel
):
    """
    Creates recipe from PANCAKE fixture
    """

    session_handler.add(strawberry_smoothie_recipe_model)
    session_handler.flush()

    return strawberry_smoothie_recipe_model


@pytest.fixture
def create_multiple_recipes(create_pancake_recipe, create_strawberry_smoothie_recipe):
    """
    Creates multiple recipes for using list finders
    """

    return [create_pancake_recipe, create_strawberry_smoothie_recipe]


def test_find_all_without_elements(recipes_repository: RecipesRepositorySQLAlchemy):
    """
    Checks user is not found if email does not exist in repository
    """

    [recipes, size] = recipes_repository.find_all()

    assert len(recipes) == 0
    assert size == 0


def test_find_all_with_one_element(
    recipes_repository: RecipesRepositorySQLAlchemy, create_pancake_recipe
):
    """
    Checks user is not found if email does not exist in repository
    """

    [recipes, size] = recipes_repository.find_all()

    assert len(recipes) == 1
    assert recipes[0].name == PANCAKE["name"]
    assert size == 1


def test_find_all_with_multiple_elements(
    recipes_repository: RecipesRepositorySQLAlchemy, create_multiple_recipes
):
    """
    Checks user is not found if email does not exist in repository
    """

    [recipes, size] = recipes_repository.find_all()

    assert len(recipes) == 2
    assert recipes[0].name == PANCAKE["name"]
    assert recipes[1].name == STRAWBERRY_SMOOTHIE["name"]
    assert size == 2


def test_find_all_with_multiple_elements_and_offset(
    recipes_repository: RecipesRepositorySQLAlchemy, create_multiple_recipes
):
    """
    Checks user is not found if email does not exist in repository
    """

    [recipes, size] = recipes_repository.find_all(offset=1)

    assert len(recipes) == 1
    assert recipes[0].name == STRAWBERRY_SMOOTHIE["name"]
    assert size == 2


def test_find_all_with_multiple_elements_and_limit(
    recipes_repository: RecipesRepositorySQLAlchemy, create_multiple_recipes
):
    """
    Checks user is not found if email does not exist in repository
    """

    [recipes, size] = recipes_repository.find_all(limit=1)

    assert len(recipes) == 1
    assert recipes[0].name == PANCAKE["name"]
    assert size == 2


def test_create_recipe(
    recipes_repository: RecipesRepositorySQLAlchemy,
    pancake_recipe_model: RecipeModel,
):
    """
    Checks user is not found if email does not exist in repository
    """

    recipe = recipes_repository.create(pancake_recipe_model.to_domain_object())

    assert recipe.uuid == PANCAKE["uuid"]
    assert recipe.name == PANCAKE["name"]
