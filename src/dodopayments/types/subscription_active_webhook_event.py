# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionActiveWebhookEvent"]


class SubscriptionActiveWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Subscription
    """Response struct representing subscription details"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["subscription.active"]
    """The event type"""
