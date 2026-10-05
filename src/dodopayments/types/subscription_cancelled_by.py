# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubscriptionCancelledBy"]


class SubscriptionCancelledBy(BaseModel):
    """The caller that cancelled a subscription or scheduled its cancel."""

    actor_type: Literal["customer", "merchant_user", "api_key", "dodo_team"]
    """The kind of caller."""

    email: Optional[str] = None
    """Email of the customer or of the dashboard user.

    `null` for an API key or the Dodo Payments team.
    """

    name: Optional[str] = None
    """Name of the customer or of the dashboard user.

    `null` for an API key or the Dodo Payments team.
    """
