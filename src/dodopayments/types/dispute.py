# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dispute"]


class Dispute(BaseModel):
    amount: str

    business_id: str

    created_at: datetime

    currency: str

    dispute_id: str

    dispute_stage: Literal["pre_dispute", "dispute", "pre_arbitration"]

    dispute_status: Literal[
        "dispute_opened",
        "dispute_expired",
        "dispute_accepted",
        "dispute_cancelled",
        "dispute_challenged",
        "dispute_won",
        "dispute_lost",
    ]

    payment_id: str
