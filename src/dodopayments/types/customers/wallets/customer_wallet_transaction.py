# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...currency import Currency

__all__ = ["CustomerWalletTransaction"]


class CustomerWalletTransaction(BaseModel):
    id: str

    after_balance: int

    amount: int

    before_balance: int

    business_id: str

    created_at: datetime

    currency: Currency

    customer_id: str

    event_type: Literal[
        "payment", "payment_reversal", "refund", "refund_reversal", "dispute", "dispute_reversal", "merchant_adjustment"
    ]

    is_credit: bool

    reason: Optional[str] = None

    reference_object_id: Optional[str] = None
