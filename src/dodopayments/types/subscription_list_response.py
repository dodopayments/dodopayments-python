# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .billing_address import BillingAddress
from .subscription_status import SubscriptionStatus
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["SubscriptionListResponse"]


class SubscriptionListResponse(BaseModel):
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
    Amount charged before tax for each recurring payment in smallest currency unit
    (e.g. cents)
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

    discount_cycles_remaining: Optional[int] = None
    """Number of remaining discount cycles if discount is applied"""

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    tax_id: Optional[str] = None
    """Tax identifier provided for this subscription (if applicable)"""
