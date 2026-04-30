# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .time_interval import TimeInterval

__all__ = [
    "EntitlementCreateResponse",
    "IntegrationConfig",
    "IntegrationConfigGitHubConfig",
    "IntegrationConfigDiscordConfig",
    "IntegrationConfigTelegramConfig",
    "IntegrationConfigFigmaConfig",
    "IntegrationConfigFramerConfig",
    "IntegrationConfigNotionConfig",
    "IntegrationConfigDigitalFilesConfig",
    "IntegrationConfigDigitalFilesConfigDigitalFiles",
    "IntegrationConfigDigitalFilesConfigDigitalFilesFile",
    "IntegrationConfigLicenseKeyConfig",
]


class IntegrationConfigGitHubConfig(BaseModel):
    permission: str

    target_id: str


class IntegrationConfigDiscordConfig(BaseModel):
    guild_id: str

    role_id: Optional[str] = None


class IntegrationConfigTelegramConfig(BaseModel):
    chat_id: str


class IntegrationConfigFigmaConfig(BaseModel):
    figma_file_id: str


class IntegrationConfigFramerConfig(BaseModel):
    framer_template_id: str


class IntegrationConfigNotionConfig(BaseModel):
    notion_template_id: str


class IntegrationConfigDigitalFilesConfigDigitalFilesFile(BaseModel):
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


class IntegrationConfigDigitalFilesConfigDigitalFiles(BaseModel):
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors
    `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin
    (`legacy` vs `ee`).
    """

    files: List[IntegrationConfigDigitalFilesConfigDigitalFilesFile]

    external_url: Optional[str] = None

    instructions: Optional[str] = None


class IntegrationConfigDigitalFilesConfig(BaseModel):
    digital_files: IntegrationConfigDigitalFilesConfigDigitalFiles
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin (`legacy`
    vs `ee`).
    """


class IntegrationConfigLicenseKeyConfig(BaseModel):
    activation_message: Optional[str] = None

    activations_limit: Optional[int] = None

    duration_count: Optional[int] = None

    duration_interval: Optional[TimeInterval] = None


IntegrationConfig: TypeAlias = Union[
    IntegrationConfigGitHubConfig,
    IntegrationConfigDiscordConfig,
    IntegrationConfigTelegramConfig,
    IntegrationConfigFigmaConfig,
    IntegrationConfigFramerConfig,
    IntegrationConfigNotionConfig,
    IntegrationConfigDigitalFilesConfig,
    IntegrationConfigLicenseKeyConfig,
]


class EntitlementCreateResponse(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    integration_config: IntegrationConfig
    """Public-facing variant of [`IntegrationConfig`].

    Mirrors every variant shape on the wire EXCEPT `DigitalFiles`, which is replaced
    with a hydrated `digital_files` object (resolved download URLs etc.). The
    persisted JSONB stays ID-only via [`IntegrationConfig`]; this enum is
    response-only.
    """

    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
    ]

    is_active: bool

    name: str

    updated_at: datetime

    description: Optional[str] = None

    metadata: Optional[object] = None
