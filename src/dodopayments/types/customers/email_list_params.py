# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailListParams"]


class EmailListParams(TypedDict, total=False):
    page_number: int
    """Which page to return. The default is 0."""

    page_size: int
    """How many emails to return. The default is 10 and the maximum is 100."""
