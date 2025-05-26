# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    archived: bool
    """List archived products"""

    brand_id: Optional[str]
    """filter by Brand id"""

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""

    recurring: Optional[bool]
    """Filter products by pricing type:

    - `true`: Show only recurring pricing products (e.g. subscriptions)
    - `false`: Show only one-time price products
    - `null` or absent: Show both types of products
    """
