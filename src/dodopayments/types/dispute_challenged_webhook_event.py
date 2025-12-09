# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .dispute import Dispute
from .._models import BaseModel

__all__ = ["DisputeChallengedWebhookEvent", "Data"]


class Data(Dispute):
    """Event-specific data"""

    payload_type: Optional[Literal["Dispute"]] = None
    """The type of payload in the data field"""


class DisputeChallengedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["dispute.challenged"]
    """The event type"""
