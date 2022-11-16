"""
Tests to check Recipe class
"""

# pylint: disable=redefined-outer-name, unused-argument

import pytest

from .recipe import Recipe, RecipeAttributes


@pytest.fixture()
def pancake() -> RecipeAttributes:
    """
    Returns a pancake recipe model
    """
    return {
        "uuid": "0aaadeb2-334e-4cc8-adf0-d11bf33c0a9e",
        "name": "Delicious pancakes",
        "favourite_amount": 100,
        "preparation_time": 90000,
        "cover": "https://path/to/image.png",
    }


@pytest.fixture()
def strawberry_smoothie() -> RecipeAttributes:
    """
    Returns a pancake recipe model
    """
    return {
        "uuid": "a3d85b8f-d50f-4779-a258-5ef9b3304fb9",
        "name": "Strawberry smoothie",
        "favourite_amount": 50,
        "preparation_time": 20000,
        "cover": "https://path/to/image.png",
    }


def test_serialize_is_ok(pancake):
    """
    Checks serialize serializes a recipe as expected
    """
    recipe = Recipe(pancake)

    result = recipe.serialize()

    assert result == pancake


def test_serialize_is_not_equal(pancake, strawberry_smoothie):
    """
    Checks serialize serializes a recipe differently of another
    """
    recipe = Recipe(strawberry_smoothie)

    result = recipe.serialize()

    assert result != pancake
