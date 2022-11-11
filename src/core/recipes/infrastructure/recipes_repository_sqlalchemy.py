"""
SQLAlchemy repository for Recipes
"""
from sqlalchemy.orm import Session
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    model = RecipeModel

    def __init__(self, session: Session):
        self.session = session

    def find_all(
        self, offset: int = None, limit: int = None
    ) -> tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """

        query = self.session.query(RecipeModel)
        count: int = query.count()
        return (
            list(
                map(
                    lambda recipe: recipe.to_domain_object(),
                    query.limit(limit).offset(offset).all(),
                )
            ),
            count,
        )

    def create(self, recipe: Recipe) -> Recipe:
        """
        Inserts a new user to the database
        """

        recipe_model = RecipeModel.from_domain_object(recipe)

        self.session.add(recipe_model)
        self.session.flush()
        self.session.refresh(recipe_model)

        return recipe_model.to_domain_object()
