"""
Recipes module dependencies
"""

from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.domain.users_repository import UsersRepository
from src.core.users.infrastructure.user_repository_sqlalchemy import (
    UsersRepositorySQLAlchemy,
)
from src.dependencies.database import get_database


def users_repository(database: Session = Depends(get_database)) -> UsersRepository:
    """
    Returns an instance of RecipesRepository
    """
    return UsersRepositorySQLAlchemy(database)


def users_registerer(
    users_repository_instance: UsersRepository = Depends(users_repository),
) -> UsersRegisterer:
    """
    Returns an instance of RecipesLister
    """
    return UsersRegisterer(users_repository_instance)
