# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .currency import Currency
from .time_interval import TimeInterval
from .subscription_status import SubscriptionStatus
from .billing_address_param import BillingAddressParam
from .addon_cart_response_item_param import AddonCartResponseItemParam
from .customer_limited_details_param import CustomerLimitedDetailsParam

__all__ = ["SubscriptionParam"]


class SubscriptionParam(TypedDict, total=False):
    addons: Required[Iterable[AddonCartResponseItemParam]]
    """Addons associated with this subscription"""

    billing: Required[BillingAddressParam]
    """Billing address details for payments"""

    cancel_at_next_billing_date: Required[bool]
    """Indicates if the subscription will cancel at the next billing date"""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the subscription was created"""

    currency: Required[Currency]
    """Currency used for the subscription payments"""

    customer: Required[CustomerLimitedDetailsParam]
    """Customer details associated with the subscription"""

    metadata: Required[Dict[str, str]]
    """Additional custom data associated with the subscription"""

    next_billing_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp of the next scheduled billing.

    Indicates the end of current billing period
    """

    on_demand: Required[bool]
    """Wether the subscription is on-demand or not"""

    payment_frequency_count: Required[int]
    """Number of payment frequency intervals"""

    payment_frequency_interval: Required[TimeInterval]
    """Time interval for payment frequency (e.g. month, year)"""

    previous_billing_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp of the last payment. Indicates the start of current billing period"""

    product_id: Required[str]
    """Identifier of the product associated with this subscription"""

    quantity: Required[int]
    """Number of units/items included in the subscription"""

    recurring_pre_tax_amount: Required[int]
    """
    Amount charged before tax for each recurring payment in smallest currency unit
    (e.g. cents)
    """

    status: Required[SubscriptionStatus]
    """Current status of the subscription"""

    subscription_id: Required[str]
    """Unique identifier for the subscription"""

    subscription_period_count: Required[int]
    """Number of subscription period intervals"""

    subscription_period_interval: Required[TimeInterval]
    """Time interval for the subscription period (e.g. month, year)"""

    tax_inclusive: Required[bool]
    """Indicates if the recurring_pre_tax_amount is tax inclusive"""

    trial_period_days: Required[int]
    """Number of days in the trial period (0 if no trial)"""

    cancelled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Cancelled timestamp if the subscription is cancelled"""

    discount_cycles_remaining: Optional[int]
    """Number of remaining discount cycles if discount is applied"""

    discount_id: Optional[str]
    """The discount id if discount is applied"""
