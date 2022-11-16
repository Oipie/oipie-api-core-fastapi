"""
BaseException
"""
from src.core.shared.infrastructure.domain_exception_category import (
    DomainExceptionCategory,
)
from src.core.shared.infrastructure.domain_exception_code import DomainExceptionCode


class DomainException(Exception):
    """
    DomainException class to create errors from
    """

    def __init__(
        self,
        message: str,
        code: DomainExceptionCode,
        category: DomainExceptionCategory,
        *args: object
    ) -> None:
        self.code = code
        self.category = category
        self.message = message
        super().__init__(message, *args)
