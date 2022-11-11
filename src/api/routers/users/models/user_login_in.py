"""
User login representation for requests
"""

from pydantic import BaseModel, EmailStr


class UserLoginIn(BaseModel):
    """
    Represents a Recipe for recipes related endpoints
    """

    email: EmailStr
    password: str
