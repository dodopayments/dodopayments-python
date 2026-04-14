# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .price import Price
from .._models import BaseModel
from .currency import Currency
from .tax_category import TaxCategory

__all__ = [
    "ProductListResponse",
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


class ProductListResponse(BaseModel):
    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    entitlements: List[Entitlement]
    """Entitlements linked to this product"""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    metadata: Dict[str, str]
    """Additional custom data associated with the product"""

    product_id: str
    """Unique identifier for the product."""

    tax_category: TaxCategory
    """Tax category associated with the product."""

    updated_at: datetime
    """Timestamp when the product was last updated."""

    currency: Optional[Currency] = None
    """Currency of the price"""

    description: Optional[str] = None
    """Description of the product, optional."""

    image: Optional[str] = None
    """URL of the product image, optional."""

    name: Optional[str] = None
    """Name of the product, optional."""

    price: Optional[int] = None
    """Price of the product, optional.

    The price is represented in the lowest denomination of the currency. For
    example:

    - In USD, a price of `$12.34` would be represented as `1234` (cents).
    - In JPY, a price of `¥1500` would be represented as `1500` (yen).
    - In INR, a price of `₹1234.56` would be represented as `123456` (paise).

    This ensures precision and avoids floating-point rounding errors.
    """

    price_detail: Optional[Price] = None
    """Details of the price"""

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive"""
