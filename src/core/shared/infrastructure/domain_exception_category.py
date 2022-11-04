from enum import Enum


class DomainExceptionCategory(Enum):
    """
    Domain exception categories
    """

    CONFLICT = "CONFLICT"
    BAD_REQUEST = "BAD_REQUEST"
    NOT_FOUND = "NOT_FOUND"
    UNKNOWN = "UNKNOWN"
