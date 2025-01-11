# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dispute"]


class Dispute(BaseModel):
    amount: str
    """
    The amount involved in the dispute, represented as a string to accommodate
    precision.
    """

    business_id: str
    """The unique identifier of the business involved in the dispute."""

    created_at: datetime
    """The timestamp of when the dispute was created, in UTC."""

    currency: str
    """The currency of the disputed amount, represented as an ISO 4217 currency code."""

    dispute_id: str
    """The unique identifier of the dispute."""

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
    """The unique identifier of the payment associated with the dispute."""
