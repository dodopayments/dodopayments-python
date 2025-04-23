# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubscriptionChangePlanParams"]


class SubscriptionChangePlanParams(TypedDict, total=False):
    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    proration_billing_mode: Required[Literal["prorated_immediately"]]

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""
