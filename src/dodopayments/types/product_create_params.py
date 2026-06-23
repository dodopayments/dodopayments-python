# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .price_param import PriceParam
from .tax_category import TaxCategory
from .metadata_param import MetadataParam
from .products.pricing_mode import PricingMode
from .license_key_duration_param import LicenseKeyDurationParam
from .attach_credit_entitlement_param import AttachCreditEntitlementParam
from .attach_product_entitlement_param import AttachProductEntitlementParam

__all__ = ["ProductCreateParams", "DigitalProductDelivery"]


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

    credit_entitlements: Optional[Iterable[AttachCreditEntitlementParam]]
    """Optional credit entitlements to attach (max 5)"""

    description: Optional[str]
    """Optional description of the product"""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered

    deprecated: use entitlements instead
    """

    entitlements: Optional[Iterable[AttachProductEntitlementParam]]
    """Optional entitlements to attach to this product (max 50)"""

    license_key_activation_message: Optional[str]
    """Optional message displayed during license key activation

    deprecated: use entitlements instead. Ignored when a `license_key` entitlement
    is attached via the `entitlements` field.
    """

    license_key_activations_limit: Optional[int]
    """The number of times the license key can be activated. Must be 0 or greater

    deprecated: use entitlements instead. Ignored when a `license_key` entitlement
    is attached via the `entitlements` field.
    """

    license_key_duration: Optional[LicenseKeyDurationParam]
    """
    Duration configuration for the license key. Set to null if you don't want the
    license key to expire. For subscriptions, the lifetime of the license key is
    tied to the subscription period

    deprecated: use entitlements instead. Ignored when a `license_key` entitlement
    is attached via the `entitlements` field.
    """

    license_key_enabled: Optional[bool]
    """When true, generates and sends a license key to your customer. Defaults to false

    deprecated: use entitlements instead. If a `license_key` entitlement is also
    attached via the `entitlements` field, the `license_key_*` config fields below
    are ignored — the attached entitlement's config is the source of truth.
    """

    metadata: MetadataParam
    """Additional metadata for the product"""

    pricing_mode: Optional[PricingMode]
    """Pricing mode for localized pricing.

    When set, rules from /products/{id}/localized-prices apply at checkout. NULL
    means base-only (existing behavior).
    """


class DigitalProductDelivery(TypedDict, total=False):
    """Choose how you would like you digital product delivered

    deprecated: use entitlements instead
    """

    external_url: Optional[str]
    """External URL to digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
