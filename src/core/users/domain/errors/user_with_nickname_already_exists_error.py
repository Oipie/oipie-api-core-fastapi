"""
UserWithNicknameAlreadyExistsError
"""
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory


class UserWithNicknameAlreadyExistsError(DomainException):
    """
    Exception raised when a user with a specific nickname already exists in repository
    """

    def __init__(self, nickname) -> None:
        super().__init__(
            f"Nickname {nickname} already exists in repository",
            "USER_WITH_NICKNAME_ALREADY_EXISTS",
            ExceptionCategory.CONFLICT,
        )
