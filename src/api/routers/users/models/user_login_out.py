"""
Recipe representation for requests
"""

from pydantic import BaseModel


class UserLoginOut(BaseModel):
    """
    Represents a Recipe for recipes related endpoints
    """

    auth_token: str

    @staticmethod
    def from_domain_object(auth_token: str):
        """
        Returns a user auth token JSONified
        """
        return UserLoginOut(auth_token=auth_token)
