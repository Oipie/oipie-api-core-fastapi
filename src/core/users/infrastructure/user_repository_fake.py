"""
Users Repository fake for testing purposes
"""
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersRepositoryFake(UsersRepository):
    """
    This class is an UsersRepository where users are stored
    in memory for testing purposes
    """

    def __init__(self, users: list[User] = None) -> None:
        self._users = [] if users is None else users

    def find_by_email(self, email: str) -> User or None:
        return next((user for user in self._users if user.email == email), None)

    def find_by_nickname(self, nickname: str) -> User or None:
        return next((user for user in self._users if user.nickname == nickname), None)

    def create(self, user: User) -> User:
        self._users.append(user)

        return user
