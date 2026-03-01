# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .ledger_entry_type import LedgerEntryType

__all__ = ["BalanceCreateLedgerEntryResponse"]


class BalanceCreateLedgerEntryResponse(BaseModel):
    """Response for creating a ledger entry"""

    id: str

    amount: str

    balance_after: str

    balance_before: str

    created_at: datetime

    credit_entitlement_id: str

    customer_id: str

    entry_type: LedgerEntryType

    is_credit: bool

    overage_after: str

    overage_before: str

    grant_id: Optional[str] = None

    reason: Optional[str] = None
