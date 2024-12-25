# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LicenseKeyInstanceListParams"]


class LicenseKeyInstanceListParams(TypedDict, total=False):
    license_key_id: Optional[str]
    """Filter by license key ID"""

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""
