# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .price import Price
from .._models import BaseModel
from .tax_category import TaxCategory
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
    "EntitlementIntegrationConfigLicenseKeyConfig",
]


class EntitlementIntegrationConfigGitHubConfig(BaseModel):
    permission: str
    """One of: pull, push, admin, maintain, triage"""

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


class EntitlementIntegrationConfigDigitalFilesConfig(BaseModel):
    digital_file_ids: List[str]

    external_url: Optional[str] = None

    instructions: Optional[str] = None


class EntitlementIntegrationConfigLicenseKeyConfig(BaseModel):
    activation_message: Optional[str] = None

    activations_limit: Optional[int] = None

    duration_count: Optional[int] = None

    duration_interval: Optional[str] = None


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
    """Summary of an entitlement attached to a product"""

    id: str

    integration_config: EntitlementIntegrationConfig
    """
    Platform-specific configuration for an entitlement. Each variant uses unique
    field names so `#[serde(untagged)]` can disambiguate correctly.
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
