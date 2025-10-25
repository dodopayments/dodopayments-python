# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionRenewedWebhookEvent", "Data"]


class Data(Subscription):
    payload_type: Optional[Literal["Subscription"]] = None
    """The type of payload in the data field"""


class SubscriptionRenewedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["subscription.renewed"]
    """The event type"""
