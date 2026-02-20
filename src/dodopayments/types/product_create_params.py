# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .currency import Currency
from .price_param import PriceParam
from .tax_category import TaxCategory
from .time_interval import TimeInterval
from .license_key_duration_param import LicenseKeyDurationParam

__all__ = ["ProductCreateParams", "CreditEntitlement", "DigitalProductDelivery"]


class ProductCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the product"""

    price: Required[PriceParam]
    """Price configuration for the product"""

    tax_category: Required[TaxCategory]
    """Tax category applied to this product"""

    addons: Optional[SequenceNotStr[str]]
    """Addons available for subscription product"""

    brand_id: Optional[str]
    """Brand id for the product, if not provided will default to primary brand"""

    credit_entitlements: Optional[Iterable[CreditEntitlement]]
    """Optional credit entitlements to attach (max 3)"""

    description: Optional[str]
    """Optional description of the product"""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered"""

    license_key_activation_message: Optional[str]
    """Optional message displayed during license key activation"""

    license_key_activations_limit: Optional[int]
    """The number of times the license key can be activated. Must be 0 or greater"""

    license_key_duration: Optional[LicenseKeyDurationParam]
    """
    Duration configuration for the license key. Set to null if you don't want the
    license key to expire. For subscriptions, the lifetime of the license key is
    tied to the subscription period
    """

    license_key_enabled: Optional[bool]
    """
    When true, generates and sends a license key to your customer. Defaults to false
    """

    metadata: Dict[str, str]
    """Additional metadata for the product"""


class CreditEntitlement(TypedDict, total=False):
    """Request struct for attaching a credit entitlement to a product"""

    credit_entitlement_id: Required[str]
    """ID of the credit entitlement to attach"""

    credits_amount: Required[str]
    """Number of credits to grant when this product is purchased"""

    credits_reduce_overage: Optional[bool]
    """Whether new credit grants reduce existing overage"""

    currency: Optional[Currency]
    """Currency for credit-related pricing"""

    expires_after_days: Optional[int]
    """Number of days after which credits expire"""

    low_balance_threshold_percent: Optional[int]
    """Balance threshold percentage for low balance notifications (0-100)"""

    max_rollover_count: Optional[int]
    """Maximum number of rollover cycles allowed"""

    overage_charge_at_billing: Optional[bool]
    """Whether overage charges are applied at billing time"""

    overage_enabled: Optional[bool]
    """Whether overage usage is allowed beyond credit balance"""

    overage_limit: Optional[str]
    """Maximum amount of overage allowed"""

    preserve_overage_at_reset: Optional[bool]
    """Whether to preserve overage balance when credits reset"""

    price_per_unit: Optional[str]
    """Price per credit unit for purchasing additional credits"""

    proration_behavior: Optional[Literal["prorate", "no_prorate"]]
    """Proration behavior for credit grants during plan changes"""

    rollover_enabled: Optional[bool]
    """Whether unused credits can roll over to the next billing period"""

    rollover_percentage: Optional[int]
    """Percentage of unused credits that can roll over (0-100)"""

    rollover_timeframe_count: Optional[int]
    """Number of timeframe units for rollover window"""

    rollover_timeframe_interval: Optional[TimeInterval]
    """Time interval for rollover window (day, week, month, year)"""

    trial_credits: Optional[str]
    """Credits granted during trial period"""

    trial_credits_expire_after_trial: Optional[bool]
    """Whether trial credits expire when trial ends"""


class DigitalProductDelivery(TypedDict, total=False):
    """Choose how you would like you digital product delivered"""

    external_url: Optional[str]
    """External URL to digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
