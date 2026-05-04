# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

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
    permission: Literal["pull", "push", "admin", "maintain", "triage"]
    """Permission to grant on the repository."""

    target_id: str
    """Repository or organisation slug to grant access to."""


class DiscordConfig(BaseModel):
    guild_id: str
    """Discord guild (server) ID."""

    role_id: Optional[str] = None
    """Optional Discord role to assign within the guild."""


class TelegramConfig(BaseModel):
    chat_id: str
    """Telegram chat ID. For groups this is typically a negative integer."""


class FigmaConfig(BaseModel):
    figma_file_id: str
    """Figma file identifier to grant access to."""


class FramerConfig(BaseModel):
    framer_template_id: str
    """Framer template identifier to grant access to."""


class NotionConfig(BaseModel):
    notion_template_id: str
    """Notion template identifier to grant access to."""


class DigitalFilesConfigDigitalFilesFile(BaseModel):
    """One file in a resolved digital-files payload."""

    download_url: str
    """Short-lived presigned URL for downloading the file."""

    expires_in: int
    """Seconds until `download_url` expires."""

    file_id: str
    """Identifier of the attached file."""

    filename: str
    """Original filename of the attached file."""

    content_type: Optional[str] = None
    """Optional content-type declared at upload."""

    file_size: Optional[int] = None
    """Optional size of the file in bytes."""


class DigitalFilesConfigDigitalFiles(BaseModel):
    """
    Populated digital-files payload with each file's metadata and a
    short-lived presigned download URL.
    """

    files: List[DigitalFilesConfigDigitalFilesFile]
    """One entry per attached file."""

    external_url: Optional[str] = None
    """Optional external URL, passed through from the entitlement configuration."""

    instructions: Optional[str] = None
    """
    Optional human-readable delivery instructions, passed through from the
    entitlement configuration.
    """


class DigitalFilesConfig(BaseModel):
    digital_files: DigitalFilesConfigDigitalFiles
    """
    Populated digital-files payload with each file's metadata and a short-lived
    presigned download URL.
    """


class LicenseKeyConfig(BaseModel):
    activation_message: Optional[str] = None
    """
    Optional message displayed when a customer activates the license key (≤ 2500
    characters).
    """

    activations_limit: Optional[int] = None
    """Maximum activations allowed per issued license key. Omit for unlimited."""

    duration_count: Optional[int] = None
    """Validity duration of issued license keys.

    Provide both `duration_count` and `duration_interval` together for a fixed
    duration; omit both for non-expiring keys.
    """

    duration_interval: Optional[TimeInterval] = None
    """Unit of `duration_count`."""


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
