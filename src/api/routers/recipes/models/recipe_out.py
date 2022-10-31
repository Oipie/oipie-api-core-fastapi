"""
Recipe representation for requests
"""

from pydantic import BaseModel
from src.core.recipes.domain.recipe import Recipe


class RecipeOut(BaseModel):
    """
    Represents a Recipe for recipes related endpoints
    """

    id: str
    name: str
    favourite_amount: int
    preparation_time: int
    cover: str or None

    @staticmethod
    def from_domain_object(recipe: Recipe):
        """
        Returns a recipe JSONified
        """
        return {
            "id": recipe.uuid,
            "name": recipe.name,
            "favourite_amount": recipe.favourite_amount,
            "preparation_time": recipe.preparation_time,
            "cover": recipe.cover,
        }
