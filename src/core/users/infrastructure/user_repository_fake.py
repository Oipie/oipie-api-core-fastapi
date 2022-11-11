"""
Users repository fake module
"""
from typing import Optional
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersRepositoryFake(UsersRepository):
    """
    This class represents a fake list implementation of a users repository
    """

    _users: list[User]

    def __init__(self, users: Optional[list[User]] = None) -> None:
        if users is None:
            users = []

        self._users = users

    def find_by_email(self, email: str) -> Optional[User]:
        """
        Tries to find an user in database by their email
        """

        return next((user for user in self._users if user.email == email), None)

    def find_by_nickname(self, nickname: str) -> Optional[User]:
        """
        Tries to find an user in database by their nickname
        """

        return next((user for user in self._users if user.nickname == nickname), None)

    def create(self, user: User) -> User:
        """
        Inserts a new user to the database
        """

        self._users.append(user)

        return user
