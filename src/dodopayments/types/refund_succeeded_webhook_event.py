# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .refund import Refund
from .._models import BaseModel

__all__ = ["RefundSucceededWebhookEvent", "Data"]


class Data(Refund):
    """Event-specific data"""

    payload_type: Optional[Literal["Refund"]] = None
    """The type of payload in the data field"""


class RefundSucceededWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["refund.succeeded"]
    """The event type"""
