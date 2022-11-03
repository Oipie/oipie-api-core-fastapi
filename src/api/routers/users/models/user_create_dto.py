"""
Data Transfer Object for User Creation
"""

from pydantic import BaseModel


class UserCreateDto(BaseModel):
    """
    UserCreateDto is a data transfer object for creating a new user.
    """

    nickname: str
    email: str
    password: str
