"""
Users Repository fake for testing purposes
"""
from typing import Optional
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersRepositoryFake(UsersRepository):
    """
    This class is an UsersRepository where users are stored
    in memory for testing purposes
    """

    _users: list[User]

    def __init__(self, users: Optional[list[User]] = None) -> None:
        if users is None:
            users = []

        self._users = users if users is None else []

    def find_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self._users if user.email == email), None)

    def find_by_nickname(self, nickname: str) -> Optional[User]:
        return next((user for user in self._users if user.nickname == nickname), None)

    def create(self, user: User) -> User:
        self._users.append(user)

        return user
