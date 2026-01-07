# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .payment import Payment
from .._models import BaseModel

__all__ = ["PaymentCancelledWebhookEvent"]


class PaymentCancelledWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Payment

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["payment.cancelled"]
    """The event type"""
