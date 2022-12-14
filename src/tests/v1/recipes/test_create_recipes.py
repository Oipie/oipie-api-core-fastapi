"""
E2E tests for recipes creation
"""


from src.api.routers.recipes.models.recipe_create_dto import RecipeCreateDto
from src.tests.fixtures.recipe_fixture import PANCAKE
from src.tests.utils.api_client import ApiClient


def test_create_recipes_works(api_client: ApiClient):
    """
    This test creates a recipe and checks that the response is the expected one
    """

    response = api_client.create_recipe(
        RecipeCreateDto(
            name=PANCAKE["name"],
            preparation_time=PANCAKE["preparation_time"],
            favourite_amount=PANCAKE["favourite_amount"],
            cover=PANCAKE["cover"],
        )
    )

    assert response["id"] is not None
    assert response["name"] == PANCAKE["name"]
    assert response["preparation_time"] == PANCAKE["preparation_time"]
    assert response["favourite_amount"] == PANCAKE["favourite_amount"]
    assert response["cover"] == PANCAKE["cover"]
