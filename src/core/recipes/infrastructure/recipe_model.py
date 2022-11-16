"""
Recipe Database Model
"""
import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.core.recipes.domain.recipe import Recipe
from src.dependencies.database import BaseModel


class RecipeModel(BaseModel):
    """
    This class represents a Recipe in database model
    """

    __tablename__ = "recipes"

    uuid = Column(
        UUID(as_uuid=True), default=uuid.uuid4, nullable=False, primary_key=True
    )
    name = Column(String, nullable=False)
    favourite_amount = Column(Integer, default=0, nullable=False)
    preparation_time = Column(Integer, default=0, nullable=False)
    cover = Column(String)

    @staticmethod
    def from_domain_object(recipe: Recipe):
        """
        Transforms to Recipe model
        """
        return RecipeModel(
            uuid=recipe.uuid,
            name=recipe.name,
            favourite_amount=recipe.favourite_amount,
            preparation_time=recipe.preparation_time,
            cover=recipe.cover,
        )

    def to_domain_object(self) -> Recipe:
        """
        Transforms Recipe database model to a domain object
        """
        return Recipe(
            {
                "uuid": str(self.uuid),
                "name": self.name,
                "favourite_amount": self.favourite_amount,
                "preparation_time": self.preparation_time,
                "cover": self.cover,
            }
        )
