"""
Test recipes creator
"""
from src.core.recipes.application.recipes_creator import (
    RecipesCreator,
    RecipesCreatorParams,
)
from src.core.recipes.infrastructure.recipes_repository_fake import (
    RecipesRepositoryFake,
)
from src.tests.fixtures.recipe_fixture import PANCAKE


def test_new_recipe_is_created():
    """
    Checks user is successfully registered by not raising an error
    """
    recipes_repository = RecipesRepositoryFake()
    recipes_creator = RecipesCreator(recipes_repository)

    created_recipe = recipes_creator.execute(
        RecipesCreatorParams(
            name=PANCAKE["name"],
            favourite_amount=PANCAKE["favourite_amount"],
            preparation_time=PANCAKE["preparation_time"],
            cover=PANCAKE["cover"],
            owner=PANCAKE["owner"],
        )
    )

    assert created_recipe.name == PANCAKE.get("name")
