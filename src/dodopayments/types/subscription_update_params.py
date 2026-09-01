# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .time_interval import TimeInterval
from .metadata_param import MetadataParam
from .subscription_status import SubscriptionStatus
from .billing_address_param import BillingAddressParam
from .cancellation_feedback import CancellationFeedback

__all__ = ["SubscriptionUpdateParams", "CreditEntitlementCart", "DisableOnDemand"]


class SubscriptionUpdateParams(TypedDict, total=False):
    billing: Optional[BillingAddressParam]

    cancel_at_next_billing_date: Optional[bool]
    """When set, the subscription will remain active until the end of billing period"""

    cancel_reason: Optional[
        Literal[
            "cancelled_by_customer",
            "cancelled_by_merchant",
            "cancelled_by_merchant_send_dunning",
            "cancelled_by_merchant_grace_period_expired",
            "dodo_team",
        ]
    ]

    cancellation_comment: Optional[str]
    """
    Free-text cancellation comment (only valid when cancelling or scheduling
    cancellation).
    """

    cancellation_feedback: Optional[CancellationFeedback]
    """
    Customer-supplied churn reason (only valid when cancelling or scheduling
    cancellation).
    """

    credit_entitlement_cart: Optional[Iterable[CreditEntitlementCart]]
    """Update credit entitlement cart settings"""

    customer_business_name: Optional[str]
    """Optional business / legal name associated with the tax id.

    When provided together with a valid tax id for a B2B subscription, this name is
    rendered on the invoice instead of the customer's personal name. Send `null` to
    explicitly clear the business name.
    """

    customer_name: Optional[str]

    disable_on_demand: Optional[DisableOnDemand]

    metadata: Optional[MetadataParam]
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """

    next_billing_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    pause: Optional[bool]
    """Removed.

    Use `status: paused` to pause and `status: active` to resume. This field always
    fails with 422, so a caller still on it gets a loud error instead of a silent
    no-op.
    """

    status: Optional[SubscriptionStatus]
    """Set to `cancelled` to cancel the subscription.

    See `cancel_reason`, `cancellation_feedback`, `cancellation_comment`, and
    `cancel_at_next_billing_date` for cancellation options.

    Set to `paused` to pause an active subscription. Set to `active` to resume a
    `paused` subscription. `active` also resumes an `on_hold` subscription that has
    an unpaid pause invoice. This voids that invoice.

    Send `paused` or `active` alone. A request that combines either with any other
    field fails with 422. `cancelled` is not exclusive this way — see
    `cancel_reason` and friends below.
    """

    subscription_period_count: Optional[int]
    """
    New number of `subscription_period_interval` units the subscription entitlement
    should span. Used together with `subscription_period_interval` to extend the
    subscription period. The resulting period must not be shorter than the current
    one (this endpoint only extends).
    """

    subscription_period_interval: Optional[TimeInterval]
    """New interval unit for the subscription period.

    When changing the period, this may be supplied alongside
    `subscription_period_count`; if omitted the existing interval is retained.
    """

    tax_id: Optional[str]


class CreditEntitlementCart(TypedDict, total=False):
    credit_entitlement_id: Required[str]

    credits_amount: Optional[str]

    expires_after_days: Optional[int]

    low_balance_threshold_percent: Optional[int]

    max_rollover_count: Optional[int]

    overage_enabled: Optional[bool]

    overage_limit: Optional[str]

    rollover_enabled: Optional[bool]

    rollover_percentage: Optional[int]

    rollover_timeframe_count: Optional[int]

    rollover_timeframe_interval: Optional[TimeInterval]
    """Unit of a duration count (e.g. license-key validity period)."""


class DisableOnDemand(TypedDict, total=False):
    next_billing_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
