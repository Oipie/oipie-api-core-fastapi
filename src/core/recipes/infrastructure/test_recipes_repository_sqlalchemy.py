"""
User repository SQLAlchemy implementation tests
"""
import pytest
from sqlalchemy.orm import Session

from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE

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
        uuid=PANCAKE["uuid"],
        name=PANCAKE["name"],
        favourite_amount=PANCAKE["favourite_amount"],
        preparation_time=PANCAKE["preparation_time"],
        cover=PANCAKE["cover"],
    )

    session_handler.add(pancake_model)
    session_handler.flush()


@pytest.fixture()
def create_strawberry_smoothie_recipe(session_handler: Session):
    """
    Creates recipe from PANCAKE fixture
    """
    strawberry_smoothie_model = RecipeModel(
        uuid=STRAWBERRY_SMOOTHIE["uuid"],
        name=STRAWBERRY_SMOOTHIE["name"],
        favourite_amount=STRAWBERRY_SMOOTHIE["favourite_amount"],
        preparation_time=STRAWBERRY_SMOOTHIE["preparation_time"],
        cover=STRAWBERRY_SMOOTHIE["cover"],
    )

    session_handler.add(strawberry_smoothie_model)
    session_handler.flush()


@pytest.fixture()
def create_multiple_recipes(create_pancake_recipe, create_strawberry_smoothie_recipe):
    """
    Creates multiple recipes for using list finders
    """


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
):
    """
    Checks user is not found if email does not exist in repository
    """

    recipe = recipes_repository.create(
        Recipe.create(
            name=PANCAKE["name"],
            cover=PANCAKE["cover"],
            preparation_time=PANCAKE["preparation_time"],
            favourite_amount=PANCAKE["favourite_amount"],
        )
    )

    assert recipe.uuid != PANCAKE["uuid"]
    assert recipe.name == PANCAKE["name"]
