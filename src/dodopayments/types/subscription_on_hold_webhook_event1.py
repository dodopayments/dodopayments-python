# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionOnHoldWebhookEvent", "Data"]


class Data(Subscription):
    """Event-specific data"""

    payload_type: Optional[Literal["Subscription"]] = None
    """The type of payload in the data field"""


class SubscriptionOnHoldWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["subscription.on_hold"]
    """The event type"""
