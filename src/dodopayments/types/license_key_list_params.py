# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseKeyListParams"]


class LicenseKeyListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter license keys created on or after this timestamp"""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter license keys created on or before this timestamp"""

    customer_id: str
    """Filter by customer ID"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""

    product_id: str
    """Filter by product ID"""

    status: Literal["active", "expired", "disabled"]
    """Filter by license key status"""
