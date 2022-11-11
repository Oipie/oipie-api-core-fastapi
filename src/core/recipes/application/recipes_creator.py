"""
Recipies Creator use case
"""
from typing import Optional, TypedDict
from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.domain.recipes_repository import RecipesRepository


class RecipesCreatorParams(TypedDict):
    """
    Recipes Creator parameters required to create a new recipe
    """

    name: str
    favourite_amount: int
    preparation_time: int
    cover: Optional[str]


class RecipesCreator:
    """
    This class returns a list of recipies
    """

    def __init__(self, recipes_repository: RecipesRepository):
        self.recipes_repository = recipes_repository

    def execute(self, recipes_creator_params: RecipesCreatorParams) -> Recipe:
        """
        Create a new recipe
        """
        new_recipe = Recipe.create(
            name=recipes_creator_params["name"],
            favourite_amount=recipes_creator_params["favourite_amount"],
            preparation_time=recipes_creator_params["preparation_time"],
            cover=recipes_creator_params["cover"],
        )

        return self.recipes_repository.create(new_recipe)
