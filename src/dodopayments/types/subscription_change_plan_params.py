# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .attach_addon_param import AttachAddonParam

__all__ = ["SubscriptionChangePlanParams"]


class SubscriptionChangePlanParams(TypedDict, total=False):
    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    proration_billing_mode: Required[Literal["prorated_immediately", "full_immediately", "difference_immediately"]]
    """Proration Billing Mode"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    addons: Optional[Iterable[AttachAddonParam]]
    """
    Addons for the new plan. Note : Leaving this empty would remove any existing
    addons
    """

    metadata: Optional[Dict[str, str]]
    """Metadata for the payment.

    If not passed, the metadata of the subscription will be taken
    """
