from enum import Enum


class DomainExceptionCode(Enum):
    """
    Domain exception codes
    """

    USER_WITH_NICKNAME_ALREADY_EXISTS = "USER_WITH_NICKNAME_ALREADY_EXISTS"
    USER_EMAIL_ALREADY_EXISTS = "USER_EMAIL_ALREADY_EXISTS"
