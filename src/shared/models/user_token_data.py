"""
Data class that contains user information from token
"""

from pydantic import BaseModel


class UserTokenData(BaseModel):
    """
    Data class that contains user information from token
    """

    email: str
    nickname: str
