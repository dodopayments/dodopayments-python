# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency

__all__ = ["PayoutListResponse"]


class PayoutListResponse(BaseModel):
    amount: int
    """The total amount of the payout."""

    business_id: str
    """The unique identifier of the business associated with the payout."""

    chargebacks: int
    """The total value of chargebacks associated with the payout."""

    created_at: datetime
    """The timestamp when the payout was created, in UTC."""

    currency: Currency

    fee: int
    """The fee charged for processing the payout."""

    payment_method: str
    """The payment method used for the payout (e.g., bank transfer, card, etc.)."""

    payout_id: str
    """The unique identifier of the payout."""

    refunds: int
    """The total value of refunds associated with the payout."""

    status: Literal["not_initiated", "in_progress", "on_hold", "failed", "success"]

    tax: int
    """The tax applied to the payout."""

    updated_at: datetime
    """The timestamp when the payout was last updated, in UTC."""

    name: Optional[str] = None
    """The name of the payout recipient or purpose."""

    payout_document_url: Optional[str] = None
    """The URL of the document associated with the payout."""

    remarks: Optional[str] = None
    """Any additional remarks or notes associated with the payout."""
