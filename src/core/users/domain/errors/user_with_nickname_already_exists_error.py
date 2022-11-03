"""
UserWithNicknameAlreadyExistsError
"""
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory


class UserWithNicknameAlreadyExistsError(DomainException):
    """
    Exception raised when a user with a specific nickname already exists in repository
    """

    category = ExceptionCategory.CONFLICT
    code = "USER_WITH_NICKNAME_ALREADY_EXISTS"

    def __init__(self, nickname) -> None:
        super().__init__(
            f"Nickname {nickname} already exists in repository",
            UserWithNicknameAlreadyExistsError.code,
            UserWithNicknameAlreadyExistsError.category,
        )
