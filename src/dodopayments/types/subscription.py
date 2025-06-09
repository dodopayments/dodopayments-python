# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .billing_address import BillingAddress
from .subscription_status import SubscriptionStatus
from .addon_cart_response_item import AddonCartResponseItem
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["Subscription"]


class Subscription(BaseModel):
    addons: List[AddonCartResponseItem]
    """Addons associated with this subscription"""

    billing: BillingAddress

    cancel_at_next_billing_date: bool
    """Indicates if the subscription will cancel at the next billing date"""

    created_at: datetime
    """Timestamp when the subscription was created"""

    currency: Currency

    customer: CustomerLimitedDetails

    metadata: Dict[str, str]

    next_billing_date: datetime
    """Timestamp of the next scheduled billing.

    Indicates the end of current billing period
    """

    on_demand: bool
    """Wether the subscription is on-demand or not"""

    payment_frequency_count: int
    """Number of payment frequency intervals"""

    payment_frequency_interval: TimeInterval

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

    subscription_id: str
    """Unique identifier for the subscription"""

    subscription_period_count: int
    """Number of subscription period intervals"""

    subscription_period_interval: TimeInterval

    tax_inclusive: bool
    """Indicates if the recurring_pre_tax_amount is tax inclusive"""

    trial_period_days: int
    """Number of days in the trial period (0 if no trial)"""

    cancelled_at: Optional[datetime] = None
    """Cancelled timestamp if the subscription is cancelled"""

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""
