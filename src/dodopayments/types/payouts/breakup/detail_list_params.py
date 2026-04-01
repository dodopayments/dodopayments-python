# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DetailListParams"]


class DetailListParams(TypedDict, total=False):
    page_number: int
    """Page number (0-indexed). Default: 0."""

    page_size: int
    """Number of items per page. Default: 10, Max: 100."""
