"""
UserCredentialsError
"""
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory


class UserCredentialsError(DomainException):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    def __init__(self) -> None:
        super().__init__(
            message="User email or password are not correct",
            code="USER_CREDENTIALS_WRONG",
            category=ExceptionCategory.BAD_REQUEST,
        )
