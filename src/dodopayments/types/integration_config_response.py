# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .time_interval import TimeInterval

__all__ = [
    "IntegrationConfigResponse",
    "GitHubConfig",
    "DiscordConfig",
    "TelegramConfig",
    "FigmaConfig",
    "FramerConfig",
    "NotionConfig",
    "DigitalFilesConfig",
    "DigitalFilesConfigDigitalFiles",
    "DigitalFilesConfigDigitalFilesFile",
    "LicenseKeyConfig",
]


class GitHubConfig(BaseModel):
    permission: str

    target_id: str


class DiscordConfig(BaseModel):
    guild_id: str

    role_id: Optional[str] = None


class TelegramConfig(BaseModel):
    chat_id: str


class FigmaConfig(BaseModel):
    figma_file_id: str


class FramerConfig(BaseModel):
    framer_template_id: str


class NotionConfig(BaseModel):
    notion_template_id: str


class DigitalFilesConfigDigitalFilesFile(BaseModel):
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


class DigitalFilesConfigDigitalFiles(BaseModel):
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors
    `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin
    (`legacy` vs `ee`).
    """

    files: List[DigitalFilesConfigDigitalFilesFile]

    external_url: Optional[str] = None

    instructions: Optional[str] = None


class DigitalFilesConfig(BaseModel):
    digital_files: DigitalFilesConfigDigitalFiles
    """Populated digital-files payload for entitlement read surfaces.

    Mirrors `DigitalProductDelivery` but is sourced from an entitlement's
    `integration_config` (not a grant) and tags each file with its origin (`legacy`
    vs `ee`).
    """


class LicenseKeyConfig(BaseModel):
    activation_message: Optional[str] = None

    activations_limit: Optional[int] = None

    duration_count: Optional[int] = None

    duration_interval: Optional[TimeInterval] = None


IntegrationConfigResponse: TypeAlias = Union[
    GitHubConfig,
    DiscordConfig,
    TelegramConfig,
    FigmaConfig,
    FramerConfig,
    NotionConfig,
    DigitalFilesConfig,
    LicenseKeyConfig,
]
