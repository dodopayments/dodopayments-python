# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .billing_address import BillingAddress
from .subscription_status import SubscriptionStatus
from .scheduled_plan_change import ScheduledPlanChange
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["SubscriptionListResponse", "Discount"]


class Discount(BaseModel):
    """
    Lightweight discount info for list endpoints.
    Array order represents position (no explicit position field).
    """

    discount_id: str
    """The unique discount ID"""

    discount_cycles_remaining: Optional[int] = None
    """Remaining billing cycles for this discount on this subscription"""


class SubscriptionListResponse(BaseModel):
    """Response struct representing subscription details"""

    billing: BillingAddress
    """Billing address details for payments"""

    cancel_at_next_billing_date: bool
    """Indicates if the subscription will cancel at the next billing date"""

    created_at: datetime
    """Timestamp when the subscription was created"""

    currency: Currency
    """Currency used for the subscription payments"""

    customer: CustomerLimitedDetails
    """Customer details associated with the subscription"""

    discounts: List[Discount]
    """All stacked discounts applied, in order of application"""

    metadata: Dict[str, str]
    """Additional custom data associated with the subscription"""

    next_billing_date: datetime
    """Timestamp of the next scheduled billing.

    Indicates the end of current billing period
    """

    on_demand: bool
    """Wether the subscription is on-demand or not"""

    payment_frequency_count: int
    """Number of payment frequency intervals"""

    payment_frequency_interval: TimeInterval
    """Time interval for payment frequency (e.g. month, year)"""

    previous_billing_date: datetime
    """Timestamp of the last payment. Indicates the start of current billing period"""

    product_id: str
    """Identifier of the product associated with this subscription"""

    quantity: int
    """Number of units/items included in the subscription"""

    recurring_pre_tax_amount: int
    """
    Amount charged before tax for each recurring payment in the currency's smallest
    unit (cents for USD, yen for JPY, fils for KWD)
    """

    status: SubscriptionStatus
    """Current status of the subscription"""

    subscription_id: str
    """Unique identifier for the subscription"""

    subscription_period_count: int
    """Number of subscription period intervals"""

    subscription_period_interval: TimeInterval
    """Time interval for the subscription period (e.g. month, year)"""

    tax_inclusive: bool
    """Indicates if the recurring_pre_tax_amount is tax inclusive"""

    trial_period_days: int
    """Number of days in the trial period (0 if no trial)"""

    cancelled_at: Optional[datetime] = None
    """Cancelled timestamp if the subscription is cancelled"""

    customer_business_name: Optional[str] = None
    """Business / legal name associated with the tax id (B2B).

    When set this is used on the invoice in place of the customer's personal name.
    """

    discount_cycles_remaining: Optional[int] = None
    """DEPRECATED: Use discounts[].cycles_remaining instead."""

    discount_id: Optional[str] = None
    """DEPRECATED: Use discounts instead."""

    payment_method_id: Optional[str] = None
    """Saved payment method id used for recurring charges"""

    product_name: Optional[str] = None
    """Name of the product associated with this subscription"""

    scheduled_change: Optional[ScheduledPlanChange] = None
    """Scheduled plan change details, if any"""

    tax_id: Optional[str] = None
    """Tax identifier provided for this subscription (if applicable)"""
