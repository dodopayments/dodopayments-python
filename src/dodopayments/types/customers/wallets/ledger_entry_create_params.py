# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ...currency import Currency

__all__ = ["LedgerEntryCreateParams"]


class LedgerEntryCreateParams(TypedDict, total=False):
    amount: Required[int]

    currency: Required[Currency]
    """Currency of the wallet to adjust"""

    entry_type: Required[Literal["credit", "debit"]]
    """Type of ledger entry - credit or debit"""

    idempotency_key: Optional[str]
    """Optional idempotency key to prevent duplicate entries"""

    reason: Optional[str]
