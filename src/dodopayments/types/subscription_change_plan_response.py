# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionChangePlanResponse"]


class SubscriptionChangePlanResponse(BaseModel):
    """Handles for a hosted checkout page that settles a plan change.

    The four fields repeat `UpdatePaymentMethodResponse` and a subset of
    `CreateSubscriptionResponse`. A shared type would rename the generated SDK
    types for all three routes, so each route keeps its own.
    """

    client_secret: Optional[str] = None
    """Client secret for an embedded checkout."""

    expires_on: Optional[datetime] = None
    """When the link stops working."""

    payment_id: Optional[str] = None
    """Id of the payment that settles the plan change."""

    payment_link: Optional[str] = None
    """Checkout page URL. Give this to the customer."""
