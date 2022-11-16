"""
Recipes module dependencies
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.recipes.application.recipes_creator import RecipesCreator
from src.core.recipes.application.recipes_lister import RecipesLister
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.dependencies.database import get_database


def recipes_repository(database: Session = Depends(get_database)) -> RecipesRepository:
    """
    Returns an instance of RecipesRepository
    """
    return RecipesRepositorySQLAlchemy(database)


def recipes_lister(
    recipes_repository_instance: RecipesRepository = Depends(recipes_repository),
) -> RecipesLister:
    """
    Returns an instance of RecipesLister
    """
    return RecipesLister(recipes_repository_instance)


def recipes_creator(
    recipes_repository_instance: RecipesRepository = Depends(recipes_repository),
) -> RecipesCreator:
    """
    Returns an instance of RecipesCreator
    """
    return RecipesCreator(recipes_repository_instance)
