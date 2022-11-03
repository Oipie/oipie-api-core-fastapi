from typing import Mapping
from fastapi import status

from src.core.shared.infrastructure.domain_exception_category import (
    DomainExceptionCategory,
)

domain_exception_category_http_map: Mapping[DomainExceptionCategory, int] = {
    DomainExceptionCategory.BAD_REQUEST: status.HTTP_400_BAD_REQUEST,
    DomainExceptionCategory.CONFLICT: status.HTTP_409_CONFLICT,
    DomainExceptionCategory.NOT_FOUND: status.HTTP_404_NOT_FOUND,
    DomainExceptionCategory.UNKNOWN: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


def get_http_status_code_by_domain_category(
    domain_exception_category: DomainExceptionCategory,
) -> int:
    """
    Get the HTTP status code from the domain exception category
    """
    return domain_exception_category_http_map.get(
        domain_exception_category, status.HTTP_500_INTERNAL_SERVER_ERROR
    )
