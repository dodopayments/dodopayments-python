# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionServicePeriod"]


class SubscriptionServicePeriod(BaseModel):
    """The service period that a payment pays for, for one subscription."""

    ends_at: datetime
    """End of the service period."""

    proration_factor: str
    """The part of one full billing period that the plan charge pays for.

    The value `"1"` is a full period. A value less than 1 is a partial period, for
    example after a plan change that keeps the billing cycle. For a plan change,
    this is the value of the new plan. The credit for the old plan is not in this
    value.
    """

    starts_at: datetime
    """Start of the service period.

    For a renewal, this is the billing date. For a plan change that applies at the
    next billing date, this is the time when the change applied. This time can be
    some minutes after the billing date.
    """

    subscription_id: str
    """Identifier of the subscription."""
