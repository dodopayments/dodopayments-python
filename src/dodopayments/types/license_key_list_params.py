# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .license_key_status import LicenseKeyStatus

__all__ = ["LicenseKeyListParams"]


class LicenseKeyListParams(TypedDict, total=False):
    customer_id: Optional[str]
    """Filter by customer ID"""

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""

    product_id: Optional[str]
    """Filter by product ID"""

    status: Optional[LicenseKeyStatus]
    """Filter by license key status"""
