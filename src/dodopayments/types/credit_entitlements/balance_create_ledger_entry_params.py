# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..metadata_param import MetadataParam
from .ledger_entry_type import LedgerEntryType

__all__ = ["BalanceCreateLedgerEntryParams"]


class BalanceCreateLedgerEntryParams(TypedDict, total=False):
    credit_entitlement_id: Required[str]

    amount: Required[str]
    """Amount to credit or debit.

    Bounded to a `NUMERIC(38,28)` column, so the integer part must have fewer than
    10 digits (< 10^10); larger values previously reached the DB and failed with a
    22003 overflow surfaced as a 500.
    """

    entry_type: Required[LedgerEntryType]
    """Entry type: credit or debit"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Expiration for credited amount (only for credit type)"""

    idempotency_key: Optional[str]
    """Idempotency key to prevent duplicate entries"""

    metadata: Optional[MetadataParam]
    """
    Optional metadata (max 50 key-value pairs, key max 40 chars, value max 500
    chars)
    """

    reason: Optional[str]
    """Human-readable reason for the entry"""
