"""
Users registerer use case
"""
from src.core.users.domain.errors.user_with_email_already_exists_error import (
    UserWithEmailAlreadyExistsError,
)
from src.core.users.domain.errors.user_with_nickname_already_exists_error import (
    UserWithNicknameAlreadyExistsError,
)
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersRegisterer:
    """
    This class creates a new user
    """

    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def __check_user_email(self, email: str):
        """
        Checks if an email is already registered
        """
        user = self.users_repository.find_by_email(email)
        if user is not None:
            raise UserWithEmailAlreadyExistsError(email)

    def __check_user_nickname(self, nickname: str):
        """
        Checks if an nickname is already registered
        """
        user = self.users_repository.find_by_nickname(nickname)
        if user is not None:
            raise UserWithNicknameAlreadyExistsError(nickname)

    def execute(self, nickname: str, email: str, password: str) -> None:
        """
        Creates a user if their nickname nor email exist in database
        """
        self.__check_user_email(email)
        self.__check_user_nickname(nickname)

        new_user = User.create(nickname, email, password=password)
        self.users_repository.create(new_user)
