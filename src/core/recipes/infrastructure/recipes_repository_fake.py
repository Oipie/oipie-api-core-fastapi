"""
ese
"""
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositoryFake(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    def __init__(self, recipes):
        self.recipes = recipes

    def find_all(self, offset: int, limit: int) -> tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """
        return list(self.recipes)[offset : (offset + limit)], len(self.recipes)
