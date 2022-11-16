"""
UserCredentialsError
"""
from src.core.shared.domain.base_exception import (
    DomainException,
    DomainExceptionCategory,
)
from src.core.shared.infrastructure.domain_exception_code import DomainExceptionCode


class UserCredentialsError(DomainException):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    def __init__(self) -> None:
        super().__init__(
            message="User email or password are not correct",
            code=DomainExceptionCode.USER_CREDENTIALS_WRONG,
            category=DomainExceptionCategory.UNAUTHORIZED,
        )
