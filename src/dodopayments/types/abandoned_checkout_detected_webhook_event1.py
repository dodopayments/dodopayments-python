# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AbandonedCheckoutDetectedWebhookEvent", "Data"]


class Data(BaseModel):
    """
    Webhook payload for abandoned_checkout.detected and abandoned_checkout.recovered events
    """

    abandoned_at: datetime

    abandonment_reason: Literal["payment_failed", "checkout_incomplete"]

    customer_id: str

    payment_id: str

    status: Literal["abandoned", "recovering", "recovered", "exhausted", "opted_out"]

    recovered_payment_id: Optional[str] = None


class AbandonedCheckoutDetectedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """
    Webhook payload for abandoned_checkout.detected and abandoned_checkout.recovered
    events
    """

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["abandoned_checkout.detected"]
    """The event type"""
