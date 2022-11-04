"""
Recipe module
"""
from typing import Optional, TypedDict


class RecipeAttributes(TypedDict):
    """
    Dictionary that represents a recipe attributes
    """

    uuid: str
    name: str
    favourite_amount: int
    preparation_time: int
    cover: Optional[str]


class Recipe:
    """
    Class to modelate a domain Recipe
    """

    def __init__(self, recipe_attributes: RecipeAttributes) -> None:
        self.uuid = recipe_attributes.get("uuid")
        self.name = recipe_attributes.get("name")
        self.favourite_amount = recipe_attributes.get("favourite_amount")
        self.preparation_time = recipe_attributes.get("preparation_time")
        self.cover = recipe_attributes.get("cover")

    def serialize(self) -> RecipeAttributes:
        """
        This method returns a recipe parsed to dict object
        """
        recipe_serialized: RecipeAttributes = {
            "uuid": self.uuid,
            "name": self.name,
            "favourite_amount": self.favourite_amount,
            "preparation_time": self.preparation_time,
            "cover": self.cover,
        }

        return recipe_serialized
