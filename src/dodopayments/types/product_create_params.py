# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .price_param import PriceParam
from .tax_category import TaxCategory
from .license_key_duration_param import LicenseKeyDurationParam
from .attach_credit_entitlement_param import AttachCreditEntitlementParam

__all__ = ["ProductCreateParams", "DigitalProductDelivery", "Entitlement"]


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
    """Optional credit entitlements to attach (max 3)"""

    description: Optional[str]
    """Optional description of the product"""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered

    deprecated: use entitlements instead
    """

    entitlements: Optional[Iterable[Entitlement]]
    """Optional entitlements to attach to this product (max 20)"""

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

    metadata: Dict[str, str]
    """Additional metadata for the product"""


class DigitalProductDelivery(TypedDict, total=False):
    """Choose how you would like you digital product delivered

    deprecated: use entitlements instead
    """

    external_url: Optional[str]
    """External URL to digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""


class Entitlement(TypedDict, total=False):
    """Request struct for attaching an entitlement to a product.

    Mirrors the `credit_entitlements` attach shape — every "attach something
    to a product" array takes objects, not bare IDs. Uniform shape leaves
    room for per-attachment settings later without another API break.
    """

    entitlement_id: Required[str]
    """ID of the entitlement to attach to the product"""
