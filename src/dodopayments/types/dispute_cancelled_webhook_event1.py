# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .dispute import Dispute
from .._models import BaseModel

__all__ = ["DisputeCancelledWebhookEvent"]


class DisputeCancelledWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Dispute

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["dispute.cancelled"]
    """The event type"""
