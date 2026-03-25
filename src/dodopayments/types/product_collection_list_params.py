# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProductCollectionListParams"]


class ProductCollectionListParams(TypedDict, total=False):
    archived: bool
    """List archived collections"""

    brand_id: str
    """Filter by Brand id"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""
