"""
Users Login use case
"""
from src.core.users.domain.errors.user_credentials_error import (
    UserCredentialsError,
)
from src.core.users.domain.users_repository import UsersRepository
from src.core.shared.services.password.password import Password
from src.core.shared.services.tokenizer.tokenizer import Tokenizer


class UsersLogin:
    """
    This class executes the flow to authenticate an user
    """

    def __init__(
        self,
        users_repository: UsersRepository,
        password_hasher: Password,
        tokenizer: Tokenizer,
    ):
        self.users_repository = users_repository
        self.password_hasher = password_hasher
        self.tokenizer = tokenizer

    def execute(self, email: str, password: str) -> str:
        """
        Creates a user if their nickname nor email exist in database
        """
        user_with_email = self.users_repository.find_by_email(email)
        if user_with_email is None:
            raise UserCredentialsError

        if not self.password_hasher.verify(user_with_email.password, password):
            raise UserCredentialsError

        return self.tokenizer.encode(user_with_email.to_payload())
