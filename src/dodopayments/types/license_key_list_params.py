# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LicenseKeyListParams"]


class LicenseKeyListParams(TypedDict, total=False):
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
