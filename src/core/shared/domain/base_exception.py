"""
BaseException
"""
from enum import Enum


class ExceptionCategory(Enum):
    """
    Exception categories classified
    """

    CONFLICT = "CONFLICT"
    BAD_REQUEST = "BAD_REQUEST"
    NOT_FOUND = "NOT_FOUND"
    UNKNOWN = "UNKNOWN"


class DomainException(Exception):
    """
    DomainException class to create errors from
    """

    def __init__(self, message: str, code: str, category: ExceptionCategory, *args: object) -> None:
        self.code = code
        self.category = category
        self.message = message
        super().__init__(message, *args)
