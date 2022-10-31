"""
Tests recipes lister
"""
from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.infrastructure.recipes_repository_fake import (
    RecipesRepositoryFake,
)
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
from src.core.recipes.application.recipes_lister import RecipesLister


def test_serialize_is_ok():
    """
    Checks that all elements are returned
    """
    recipes = [Recipe(PANCAKE), Recipe(STRAWBERRY_SMOOTHIE)]
    recipe_repository = RecipesRepositoryFake(recipes)
    recipe_lister = RecipesLister(recipe_repository)

    recipes, total_recipes = recipe_lister.execute(offset=0, limit=10)

    assert total_recipes == 2
    assert len(recipes) == 2
    assert recipes[0].name == PANCAKE.get("name")
    assert recipes[1].name == STRAWBERRY_SMOOTHIE.get("name")
