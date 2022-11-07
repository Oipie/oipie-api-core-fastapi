"""
Recipes repository fake module
"""
from typing import Optional
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositoryFake(RecipesRepository):
    """
    This class represents a fake implementation of a recipes repository
    """

    _recipes: list[Recipe]

    def __init__(self, recipes: Optional[list[Recipe]] = None):
        if recipes is None:
            recipes = []

        self._recipes = recipes

    def find_all(self, offset: int, limit: int) -> tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """

        return list(self._recipes)[offset : (offset + limit)], len(self._recipes)

    def create(self, recipe: Recipe) -> Recipe:
        """
        Inserts a new user to the database
        """

        self._recipes.append(recipe)

        return recipe
