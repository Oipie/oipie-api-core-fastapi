"""
E2E tests for recipes index
"""

import pytest

from src.api.routers.recipes.models.recipe_create_dto import RecipeCreateDto
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
from src.tests.utils.api_client import ApiClient


@pytest.fixture()
def create_pancake(api_client: ApiClient):
    """
    Creates pancake recipe
    """

    api_client.create_recipe(
        RecipeCreateDto(
            name=PANCAKE["name"],
            preparation_time=PANCAKE["preparation_time"],
            favourite_amount=PANCAKE["favourite_amount"],
            cover=PANCAKE["cover"],
        )
    )


@pytest.fixture()
def create_strawberry_smoothie(api_client: ApiClient):
    """
    Creates strawberry smoothie recipe
    """

    api_client.create_recipe(
        RecipeCreateDto(
            name=STRAWBERRY_SMOOTHIE["name"],
            preparation_time=STRAWBERRY_SMOOTHIE["preparation_time"],
            favourite_amount=STRAWBERRY_SMOOTHIE["favourite_amount"],
            cover=STRAWBERRY_SMOOTHIE["cover"],
        )
    )


def test_index_recipes_works(api_client: ApiClient):
    """
    This test checks response when there are no recipes
    """

    response = api_client.get_recipes()

    assert response["items"] == []
    assert response["total_items"] == 0


def test_index_recipes_works_with_recipes(
    create_pancake, create_strawberry_smoothie, api_client: ApiClient
):
    """
    This test checks response when there are no recipes
    """

    response = api_client.get_recipes()

    assert isinstance(response["items"], list)
    assert len(response["items"]) == 2
    assert response["items"][0]["name"] == PANCAKE["name"]
    assert response["items"][1]["name"] == STRAWBERRY_SMOOTHIE["name"]
    assert response["total_items"] == 2
