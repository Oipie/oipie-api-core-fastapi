"""
Users Finder use case
"""
from src.core.users.domain.errors.user_not_found_error import UserNotFoundError
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersFinder:
    """
    This class executes the flow to authenticate an user
    """

    def __init__(
        self,
        users_repository: UsersRepository,
    ):
        self.users_repository = users_repository

    def execute(self, email: str) -> User:
        """
        Creates a user if their nickname nor email exist in database
        """
        user = self.users_repository.find_by_email(email)
        if user is None:
            raise UserNotFoundError(email)

        return user
