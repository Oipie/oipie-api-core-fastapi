"""
Data Transfer Object for User Creation
"""

from pydantic import BaseModel, EmailStr


class UserCreateDto(BaseModel):
    """
    UserCreateDto is a data transfer object for creating a new user.
    """

    nickname: str
    email: EmailStr
    password: str
