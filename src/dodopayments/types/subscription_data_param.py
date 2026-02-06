# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .on_demand_subscription_param import OnDemandSubscriptionParam

__all__ = ["SubscriptionDataParam"]


class SubscriptionDataParam(TypedDict, total=False):
    on_demand: Optional[OnDemandSubscriptionParam]

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """
