# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionRenewedWebhookEvent", "Data"]


class Data(Subscription):
    """Subscription payload sent on a webhook.

    It carries every field of
    `SubscriptionResponse`, plus the grace-period deadline.
    """

    past_due_ends_at: Optional[datetime] = None
    """Time when the grace period ends.

    The subscription moves to `on_hold` or to `cancelled` at this time.

    Read in the same query as the rest of the payload, so it always comes from the
    row snapshot that produced `status`. It is set whenever the subscription sits in
    a window at that moment. A delayed event of another type therefore carries the
    deadline too, next to a `past_due` status.
    """


class SubscriptionRenewedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Subscription payload sent on a webhook.

    It carries every field of `SubscriptionResponse`, plus the grace-period
    deadline.
    """

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["subscription.renewed"]
    """The event type"""
