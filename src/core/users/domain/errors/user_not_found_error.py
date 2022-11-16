"""
UserWithEmailAlreadyExistsError
"""
from src.core.shared.domain.base_exception import DomainException
from src.core.shared.infrastructure.domain_exception_category import (
    DomainExceptionCategory,
)
from src.core.shared.infrastructure.domain_exception_code import DomainExceptionCode


# TODO Errors in python should by `...Exception` format
class UserNotFoundError(DomainException):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    category = DomainExceptionCategory.NOT_FOUND
    code = DomainExceptionCode.USER_NOT_FOUND

    def __init__(self, email) -> None:
        super().__init__(
            f"User with email {email} not found",
            UserNotFoundError.code,
            UserNotFoundError.category,
        )
