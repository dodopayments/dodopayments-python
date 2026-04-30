# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .time_interval import TimeInterval
from .subscription_status import SubscriptionStatus
from .billing_address_param import BillingAddressParam
from .cancellation_feedback import CancellationFeedback

__all__ = ["SubscriptionUpdateParams", "CreditEntitlementCart", "DisableOnDemand"]


class SubscriptionUpdateParams(TypedDict, total=False):
    billing: Optional[BillingAddressParam]

    cancel_at_next_billing_date: Optional[bool]
    """When set, the subscription will remain active until the end of billing period"""

    cancel_reason: Optional[
        Literal["cancelled_by_customer", "cancelled_by_merchant", "cancelled_by_merchant_send_dunning", "dodo_team"]
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

    customer_name: Optional[str]

    disable_on_demand: Optional[DisableOnDemand]

    metadata: Optional[Dict[str, str]]

    next_billing_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    status: Optional[SubscriptionStatus]

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


class DisableOnDemand(TypedDict, total=False):
    next_billing_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
