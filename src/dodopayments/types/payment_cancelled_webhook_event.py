# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .payment import Payment
from .._models import BaseModel

__all__ = ["PaymentCancelledWebhookEvent", "Data"]


class Data(Payment):
    payload_type: Optional[Literal["Payment"]] = None
    """The type of payload in the data field"""


class PaymentCancelledWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["payment.cancelled"]
    """The event type"""
