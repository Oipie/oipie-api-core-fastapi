"""
Recipes module dependencies
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.shared.services.password.dependencies import password_hasher
from src.core.shared.services.password.password import Password
from src.core.shared.services.tokenizer.dependencies import tokenizer
from src.core.shared.services.tokenizer.tokenizer import Tokenizer
from src.core.users.application.users_finder import UsersFinder
from src.core.users.application.users_login import UsersLogin
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
    password_hasher_instance: Password = Depends(password_hasher),
) -> UsersRegisterer:
    """
    Returns an instance of RecipesLister
    """
    return UsersRegisterer(users_repository_instance, password_hasher_instance)


def users_login(
    users_repository_instance: UsersRepository = Depends(users_repository),
    password_hasher_instance: Password = Depends(password_hasher),
    tokenizer_instance: Tokenizer = Depends(tokenizer),
) -> UsersLogin:
    """
    Returns an instance of UsersLogin
    """
    return UsersLogin(
        users_repository_instance,
        password_hasher_instance,
        tokenizer_instance,
    )


def users_finder(
    users_repository_instance: UsersRepository = Depends(users_repository),
) -> UsersFinder:
    """
    Returns an instance of UsersLogin
    """
    return UsersFinder(
        users_repository_instance,
    )
