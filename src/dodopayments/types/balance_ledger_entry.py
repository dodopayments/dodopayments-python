# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency

__all__ = ["BalanceLedgerEntry"]


class BalanceLedgerEntry(BaseModel):
    id: str

    amount: int

    business_id: str

    created_at: datetime

    currency: Currency

    event_type: Literal[
        "payment",
        "refund",
        "refund_reversal",
        "dispute",
        "dispute_reversal",
        "tax",
        "tax_reversal",
        "payment_fees",
        "refund_fees",
        "refund_fees_reversal",
        "dispute_fees",
        "payout",
        "payout_fees",
        "payout_reversal",
        "payout_fees_reversal",
        "dodo_credits",
        "adjustment",
        "currency_conversion",
    ]

    is_credit: bool

    usd_equivalent_amount: int

    after_balance: Optional[int] = None

    before_balance: Optional[int] = None

    description: Optional[str] = None

    reference_object_id: Optional[str] = None
