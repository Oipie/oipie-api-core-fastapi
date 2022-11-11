"""
User login representation for requests
"""

from pydantic import BaseModel


class UserLoginIn(BaseModel):
    """
    Represents a Recipe for recipes related endpoints
    """

    email: str
    password: str
