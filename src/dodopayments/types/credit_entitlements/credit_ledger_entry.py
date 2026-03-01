# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditLedgerEntry"]


class CreditLedgerEntry(BaseModel):
    """Response for a ledger entry"""

    id: str

    amount: str

    balance_after: str

    balance_before: str

    business_id: str

    created_at: datetime

    credit_entitlement_id: str

    customer_id: str

    is_credit: bool

    overage_after: str

    overage_before: str

    transaction_type: Literal[
        "credit_added",
        "credit_deducted",
        "credit_expired",
        "credit_rolled_over",
        "rollover_forfeited",
        "overage_charged",
        "auto_top_up",
        "manual_adjustment",
        "refund",
    ]

    description: Optional[str] = None

    grant_id: Optional[str] = None

    reference_id: Optional[str] = None

    reference_type: Optional[str] = None
