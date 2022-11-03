"""
UserWithEmailAlreadyExistsError
"""
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory


class UserWithEmailAlreadyExistsError(DomainException):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    def __init__(self, email) -> None:
        super().__init__(
            f"Email {email} already exists in repository",
            "USER_EMAIL_ALREADY_EXISTS",
            ExceptionCategory.CONFLICT,
        )
