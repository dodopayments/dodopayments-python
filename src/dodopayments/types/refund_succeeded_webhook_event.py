# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .refund import Refund
from .._models import BaseModel

__all__ = ["RefundSucceededWebhookEvent"]


class RefundSucceededWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Refund

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["refund.succeeded"]
    """The event type"""
