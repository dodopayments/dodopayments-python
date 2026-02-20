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

__all__ = ["ProductUpdateParams", "CreditEntitlement", "DigitalProductDelivery"]


class ProductUpdateParams(TypedDict, total=False):
    addons: Optional[SequenceNotStr[str]]
    """Available Addons for subscription products"""

    brand_id: Optional[str]

    credit_entitlements: Optional[Iterable[CreditEntitlement]]
    """
    Credit entitlements to update (replaces all existing when present) Send empty
    array to remove all, omit field to leave unchanged
    """

    description: Optional[str]
    """Description of the product, optional and must be at most 1000 characters."""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered"""

    image_id: Optional[str]
    """Product image id after its uploaded to S3"""

    license_key_activation_message: Optional[str]
    """Message sent to the customer upon license key activation.

    Only applicable if `license_key_enabled` is `true`. This message contains
    instructions for activating the license key.
    """

    license_key_activations_limit: Optional[int]
    """Limit for the number of activations for the license key.

    Only applicable if `license_key_enabled` is `true`. Represents the maximum
    number of times the license key can be activated.
    """

    license_key_duration: Optional[LicenseKeyDurationParam]
    """Duration of the license key if enabled.

    Only applicable if `license_key_enabled` is `true`. Represents the duration in
    days for which the license key is valid.
    """

    license_key_enabled: Optional[bool]
    """Whether the product requires a license key.

    If `true`, additional fields related to license key (duration, activations
    limit, activation message) become applicable.
    """

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the product"""

    name: Optional[str]
    """Name of the product, optional and must be at most 100 characters."""

    price: Optional[PriceParam]
    """Price details of the product."""

    tax_category: Optional[TaxCategory]
    """Tax category of the product."""


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

    files: Optional[SequenceNotStr[str]]
    """Uploaded files ids of digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
