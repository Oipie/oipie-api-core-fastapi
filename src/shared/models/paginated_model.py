"""
Paginated respose representation for requests
"""

from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")


class PaginatedModel(GenericModel, Generic[T]):
    """
    Represents a list of models within their metadata
    """

    items: list[T]
    total_items: int

    @staticmethod
    def serialize(items: list[T], total_items: int):
        """
        Returns items JSONified
        """
        return {"items": items, "total_items": total_items}
