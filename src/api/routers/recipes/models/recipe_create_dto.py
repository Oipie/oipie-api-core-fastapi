"""
Data Transfer Object for User Creation
"""

from typing import Optional

from pydantic import BaseModel


class RecipeCreateDto(BaseModel):
    """
    Data Transfer Object for User Creation
    """

    name: str
    favourite_amount: int
    preparation_time: int
    cover: Optional[str]
