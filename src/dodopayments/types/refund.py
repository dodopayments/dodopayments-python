# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .metadata import Metadata
from .refund_status import RefundStatus
from .customer_limited_details import CustomerLimitedDetails
from .refund_network_reference_type import RefundNetworkReferenceType

__all__ = ["Refund"]


class Refund(BaseModel):
    brand_id: str
    """Brand id this refund belongs to"""

    business_id: str
    """The unique identifier of the business issuing the refund."""

    created_at: datetime
    """The timestamp of when the refund was created in UTC."""

    customer: CustomerLimitedDetails
    """Details about the customer for this refund (from the associated payment)"""

    is_partial: bool
    """If true the refund is a partial refund"""

    metadata: Metadata
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

    network_reference: Optional[str] = None
    """The reference number that the card network or the bank gives to the refund.

    The customer can give this number to their bank to trace the refund. It is null
    until the payment processor sends it.
    """

    network_reference_type: Optional[RefundNetworkReferenceType] = None
    """The kind of `network_reference`: ARN, STAN or RRN."""

    reason: Optional[str] = None
    """The reason provided for the refund, if any. Optional."""
