# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter customers created on or after this timestamp"""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter customers created on or before this timestamp"""

    email: str
    """Filter by customer email"""

    name: str
    """Filter by customer name (partial match, case-insensitive)"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""
