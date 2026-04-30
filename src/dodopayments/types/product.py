# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .price import Price
from .._models import BaseModel
from .tax_category import TaxCategory
from .time_interval import TimeInterval
from .license_key_duration import LicenseKeyDuration
from .digital_product_delivery import DigitalProductDelivery
from .credit_entitlement_mapping_response import CreditEntitlementMappingResponse

__all__ = [
    "Product",
    "Entitlement",
    "EntitlementIntegrationConfig",
    "EntitlementIntegrationConfigGitHubConfig",
    "EntitlementIntegrationConfigDiscordConfig",
    "EntitlementIntegrationConfigTelegramConfig",
    "EntitlementIntegrationConfigFigmaConfig",
    "EntitlementIntegrationConfigFramerConfig",
    "EntitlementIntegrationConfigNotionConfig",
    "EntitlementIntegrationConfigDigitalFilesConfig",
    "EntitlementIntegrationConfigDigitalFilesConfigDigitalFiles",
    "EntitlementIntegrationConfigDigitalFilesConfigDigitalFilesFile",
    "EntitlementIntegrationConfigLicenseKeyConfig",
]


class EntitlementIntegrationConfigGitHubConfig(BaseModel):
    permission: str

    target_id: str


class EntitlementIntegrationConfigDiscordConfig(BaseModel):
    guild_id: str

    role_id: Optional[str] = None


class EntitlementIntegrationConfigTelegramConfig(BaseModel):
    chat_id: str


class EntitlementIntegrationConfigFigmaConfig(BaseModel):
    figma_file_id: str


class EntitlementIntegrationConfigFramerConfig(BaseModel):
    framer_template_id: str


class EntitlementIntegrationConfigNotionConfig(BaseModel):
    notion_template_id: str


class EntitlementIntegrationConfigDigitalFilesConfigDigitalFilesFile(BaseModel):
    download_url: str

    expires_in: int
    """Seconds until `download_url` expires."""

    file_id: str

    filename: str

    source: str
    """
    `"legacy"` for files in `product_files`, `"ee"` for files managed by the
    Entitlements Engine.
    """

    content_type: Optional[str] = None

    file_size: Optional[int] = None


class EntitlementIntegrationConfigDigitalFilesConfigDigitalFiles(BaseModel):
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors
    `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin
    (`legacy` vs `ee`).
    """

    files: List[EntitlementIntegrationConfigDigitalFilesConfigDigitalFilesFile]

    external_url: Optional[str] = None

    instructions: Optional[str] = None


class EntitlementIntegrationConfigDigitalFilesConfig(BaseModel):
    digital_files: EntitlementIntegrationConfigDigitalFilesConfigDigitalFiles
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin (`legacy`
    vs `ee`).
    """


class EntitlementIntegrationConfigLicenseKeyConfig(BaseModel):
    activation_message: Optional[str] = None

    activations_limit: Optional[int] = None

    duration_count: Optional[int] = None

    duration_interval: Optional[TimeInterval] = None


EntitlementIntegrationConfig: TypeAlias = Union[
    EntitlementIntegrationConfigGitHubConfig,
    EntitlementIntegrationConfigDiscordConfig,
    EntitlementIntegrationConfigTelegramConfig,
    EntitlementIntegrationConfigFigmaConfig,
    EntitlementIntegrationConfigFramerConfig,
    EntitlementIntegrationConfigNotionConfig,
    EntitlementIntegrationConfigDigitalFilesConfig,
    EntitlementIntegrationConfigLicenseKeyConfig,
]


class Entitlement(BaseModel):
    """Summary of an entitlement attached to a product.

    `integration_config` uses [`IntegrationConfigResponse`] (NOT the
    persisted [`IntegrationConfig`]) so digital_files entitlements embed the
    resolved `digital_files` object — matching what `GET /entitlements/{id}`
    returns. All other variants pass through unchanged via
    `#[serde(untagged)]`.
    """

    id: str

    integration_config: EntitlementIntegrationConfig
    """Public-facing variant of [`IntegrationConfig`].

    Mirrors every variant shape on the wire EXCEPT `DigitalFiles`, which is replaced
    with a hydrated `digital_files` object (resolved download URLs etc.). The
    persisted JSONB stays ID-only via [`IntegrationConfig`]; this enum is
    response-only.
    """

    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
    ]

    name: str

    description: Optional[str] = None


class Product(BaseModel):
    brand_id: str

    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    credit_entitlements: List[CreditEntitlementMappingResponse]
    """Attached credit entitlements with settings"""

    entitlements: List[Entitlement]
    """Attached entitlements (integration-based access grants)"""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    license_key_enabled: bool
    """Indicates whether the product requires a license key."""

    metadata: Dict[str, str]
    """Additional custom data associated with the product"""

    price: Price
    """Pricing information for the product."""

    product_id: str
    """Unique identifier for the product."""

    tax_category: TaxCategory
    """Tax category associated with the product."""

    updated_at: datetime
    """Timestamp when the product was last updated."""

    addons: Optional[List[str]] = None
    """Available Addons for subscription products"""

    description: Optional[str] = None
    """Description of the product, optional."""

    digital_product_delivery: Optional[DigitalProductDelivery] = None
    """Digital-product-delivery payload for a grant.

    Populated for grants whose entitlement has `integration_type = 'digital_files'`.
    `files` carries presigned download URLs; the source (EE service or legacy
    in-process S3 presigning) is opaque to the caller.
    """

    image: Optional[str] = None
    """URL of the product image, optional."""

    license_key_activation_message: Optional[str] = None
    """Message sent upon license key activation, if applicable."""

    license_key_activations_limit: Optional[int] = None
    """Limit on the number of activations for the license key, if enabled."""

    license_key_duration: Optional[LicenseKeyDuration] = None
    """Duration of the license key validity, if enabled."""

    name: Optional[str] = None
    """Name of the product, optional."""

    product_collection_id: Optional[str] = None
    """The product collection ID this product belongs to, if any"""
