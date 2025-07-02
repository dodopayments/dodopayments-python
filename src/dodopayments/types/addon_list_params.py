# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AddonListParams"]


class AddonListParams(TypedDict, total=False):
    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""
