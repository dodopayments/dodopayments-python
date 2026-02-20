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

__all__ = ["Subscription", "CreditEntitlementCart", "MeterCreditEntitlementCart", "Meter", "CustomFieldResponse"]


class CreditEntitlementCart(BaseModel):
    """Response struct representing credit entitlement cart details for a subscription"""

    credit_entitlement_id: str

    credit_entitlement_name: str

    credits_amount: str

    overage_balance: str
    """Customer's current overage balance for this entitlement"""

    overage_charge_at_billing: bool

    overage_enabled: bool

    product_id: str

    remaining_balance: str
    """Customer's current remaining credit balance for this entitlement"""

    rollover_enabled: bool

    unit: str
    """Unit label for the credit entitlement (e.g., "API Calls", "Tokens")"""

    expires_after_days: Optional[int] = None

    low_balance_threshold_percent: Optional[int] = None

    max_rollover_count: Optional[int] = None

    overage_limit: Optional[str] = None

    rollover_percentage: Optional[int] = None

    rollover_timeframe_count: Optional[int] = None

    rollover_timeframe_interval: Optional[TimeInterval] = None


class MeterCreditEntitlementCart(BaseModel):
    """
    Response struct representing meter-credit entitlement mapping cart details for a subscription
    """

    credit_entitlement_id: str

    meter_id: str

    meter_name: str

    meter_units_per_credit: str

    product_id: str


class Meter(BaseModel):
    """Response struct representing usage-based meter cart details for a subscription"""

    currency: Currency

    free_threshold: int

    measurement_unit: str

    meter_id: str

    name: str

    price_per_unit: str

    description: Optional[str] = None


class CustomFieldResponse(BaseModel):
    """Customer's response to a custom field"""

    key: str
    """Key matching the custom field definition"""

    value: str
    """Value provided by customer"""


class Subscription(BaseModel):
    """Response struct representing subscription details"""

    addons: List[AddonCartResponseItem]
    """Addons associated with this subscription"""

    billing: BillingAddress
    """Billing address details for payments"""

    cancel_at_next_billing_date: bool
    """Indicates if the subscription will cancel at the next billing date"""

    created_at: datetime
    """Timestamp when the subscription was created"""

    credit_entitlement_cart: List[CreditEntitlementCart]
    """Credit entitlement cart settings for this subscription"""

    currency: Currency
    """Currency used for the subscription payments"""

    customer: CustomerLimitedDetails
    """Customer details associated with the subscription"""

    metadata: Dict[str, str]
    """Additional custom data associated with the subscription"""

    meter_credit_entitlement_cart: List[MeterCreditEntitlementCart]
    """Meter credit entitlement cart settings for this subscription"""

    meters: List[Meter]
    """Meters associated with this subscription (for usage-based billing)"""

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

    custom_field_responses: Optional[List[CustomFieldResponse]] = None
    """Customer's responses to custom fields collected during checkout"""

    discount_cycles_remaining: Optional[int] = None
    """Number of remaining discount cycles if discount is applied"""

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    expires_at: Optional[datetime] = None
    """Timestamp when the subscription will expire"""

    payment_method_id: Optional[str] = None
    """Saved payment method id used for recurring charges"""

    tax_id: Optional[str] = None
    """Tax identifier provided for this subscription (if applicable)"""
