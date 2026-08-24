# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .metadata_param import MetadataParam
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

    cancel_scheduled_change_plan: bool
    """Replace a scheduled plan change with this one.

    The scheduled change is cancelled by the transaction that applies this change. A
    change that never applies leaves the schedule in place.

    `effective_at: next_billing_date` is allowed. The new schedule then replaces the
    old one in the request transaction.

    A pending plan change still gets a `409`. This field does not affect it.

    The preview route shares this request body, so a preview that sets this field
    also passes the scheduled-change `409`.
    """

    collect_via_payment_link: bool
    """Collect the plan-change amount with a payment link.

    The customer then pays on a checkout page.

    The business needs the `allow_plan_change_via_payment_link` capability. The
    request needs `effective_at: immediately`. The request also needs
    `on_payment_failure: prevent_change`.

    The preview route shares this request body and ignores this field.
    """

    discount_code: Optional[str]
    """DEPRECATED: Use discount_codes instead.

    Cannot be used together with discount_codes.
    """

    discount_codes: Optional[SequenceNotStr[str]]
    """Stacked discount codes to apply to the new plan.

    Max 20. Cannot be used together with discount_code. If provided, replaces any
    existing discount codes. Empty array removes all discounts. If not provided
    (None), existing discounts with preserve_on_plan_change=true are preserved.
    """

    effective_at: Literal["immediately", "next_billing_date"]
    """When to apply the plan change.

    - `immediately` (default): Apply the plan change right away
    - `next_billing_date`: Schedule the change for the next billing date
    """

    metadata: Optional[MetadataParam]
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
