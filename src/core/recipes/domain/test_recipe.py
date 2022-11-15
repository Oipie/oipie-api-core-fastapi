"""
Tests to check Recipe class
"""

# pylint: disable=redefined-outer-name, unused-argument

import pytest

from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
from .recipe import Recipe, RecipeAttributes


@pytest.fixture()
def pancake() -> RecipeAttributes:
    """
    Returns a pancake recipe model
    """
    return PANCAKE


@pytest.fixture()
def strawberry_smoothie() -> RecipeAttributes:
    """
    Returns a strawberry smoothie recipe model
    """
    return STRAWBERRY_SMOOTHIE


def test_serialize_is_ok(pancake):
    """
    Checks serialize serializes a recipe as expected
    """
    recipe = Recipe(recipe_attributes=pancake)

    result = recipe.serialize()

    assert result == pancake


def test_serialize_is_not_equal(pancake, strawberry_smoothie):
    """
    Checks serialize serializes a recipe differently of another
    """
    recipe = Recipe(strawberry_smoothie)

    result = recipe.serialize()

    assert result != pancake
