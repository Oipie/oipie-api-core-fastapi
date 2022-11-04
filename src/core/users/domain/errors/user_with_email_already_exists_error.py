"""
UserWithEmailAlreadyExistsError
"""
from src.core.shared.domain.base_exception import DomainException
from src.core.shared.infrastructure.domain_exception_category import (
    DomainExceptionCategory,
)
from src.core.shared.infrastructure.domain_exception_code import DomainExceptionCode


class UserWithEmailAlreadyExistsError(DomainException):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    category = DomainExceptionCategory.CONFLICT
    code = DomainExceptionCode.USER_EMAIL_ALREADY_EXISTS

    def __init__(self, email) -> None:
        super().__init__(
            f"Email {email} already exists in repository",
            UserWithEmailAlreadyExistsError.code,
            UserWithEmailAlreadyExistsError.category,
        )
