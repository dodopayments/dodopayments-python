# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .attach_addon_param import AttachAddonParam

__all__ = ["SubscriptionPreviewChangePlanParams"]


class SubscriptionPreviewChangePlanParams(TypedDict, total=False):
    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    proration_billing_mode: Required[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ]
    """Proration Billing Mode"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    adaptive_currency_fees_inclusive: Optional[bool]
    """
    Whether adaptive currency fees should be included in the price (true) or added
    on top (false). If not specified, uses the subscription's stored setting.
    """

    addons: Optional[Iterable[AttachAddonParam]]
    """
    Addons for the new plan. Note : Leaving this empty would remove any existing
    addons
    """

    discount_code: Optional[str]
    """
    Optional discount code to apply to the new plan. If provided, validates and
    applies the discount to the plan change. If not provided and the subscription
    has an existing discount with `preserve_on_plan_change=true`, the existing
    discount will be preserved (if applicable to the new product).
    """

    effective_at: Literal["immediately", "next_billing_date"]
    """When to apply the plan change.

    - `immediately` (default): Apply the plan change right away
    - `next_billing_date`: Schedule the change for the next billing date
    """

    metadata: Optional[Dict[str, str]]
    """Metadata for the payment.

    If not passed, the metadata of the subscription will be taken
    """

    on_payment_failure: Optional[Literal["prevent_change", "apply_change"]]
    """Controls behavior when the plan change payment fails.

    - `prevent_change`: Keep subscription on current plan until payment succeeds
    - `apply_change` (default): Apply plan change immediately regardless of payment
      outcome

    If not specified, uses the business-level default setting.
    """
