# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .refund_status import RefundStatus
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["Refund"]


class Refund(BaseModel):
    business_id: str
    """The unique identifier of the business issuing the refund."""

    created_at: datetime
    """The timestamp of when the refund was created in UTC."""

    customer: CustomerLimitedDetails
    """Details about the customer for this refund (from the associated payment)"""

    is_partial: bool
    """If true the refund is a partial refund"""

    metadata: Dict[str, str]
    """Additional metadata stored with the refund."""

    payment_id: str
    """The unique identifier of the payment associated with the refund."""

    refund_id: str
    """The unique identifier of the refund."""

    status: RefundStatus
    """The current status of the refund."""

    amount: Optional[int] = None
    """The refunded amount."""

    currency: Optional[Currency] = None
    """The currency of the refund, represented as an ISO 4217 currency code."""

    reason: Optional[str] = None
    """The reason provided for the refund, if any. Optional."""
