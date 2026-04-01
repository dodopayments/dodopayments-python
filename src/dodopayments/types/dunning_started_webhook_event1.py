# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DunningStartedWebhookEvent", "Data"]


class Data(BaseModel):
    """Webhook payload for dunning.started and dunning.recovered events"""

    created_at: datetime

    customer_id: str

    status: Literal["recovering", "recovered", "exhausted"]

    subscription_id: str

    trigger_state: Literal["on_hold", "cancelled"]

    payment_id: Optional[str] = None


class DunningStartedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Webhook payload for dunning.started and dunning.recovered events"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["dunning.started"]
    """The event type"""
