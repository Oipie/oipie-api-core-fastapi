"""
Data Transfer Object for User
"""

from pydantic import BaseModel

from src.core.users.domain.user import User


class UserResponseDto(BaseModel):
    """
    UserResponseDto is a data transfer object to send .
    """

    id: str
    nickname: str
    email: str

    @staticmethod
    def from_domain_object(user: User):
        """
        Returns a user JSONified
        """

        return UserResponseDto(
            id=user.uuid,
            nickname=user.nickname,
            email=user.email,
        )
