# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...currency import Currency

__all__ = ["LedgerEntryListParams"]


class LedgerEntryListParams(TypedDict, total=False):
    currency: Currency
    """Optional currency filter"""

    page_number: int

    page_size: int
