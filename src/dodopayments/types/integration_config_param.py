# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .time_interval import TimeInterval

__all__ = [
    "IntegrationConfigParam",
    "GitHubConfig",
    "DiscordConfig",
    "TelegramConfig",
    "FigmaConfig",
    "FramerConfig",
    "NotionConfig",
    "DigitalFilesConfig",
    "LicenseKeyConfig",
]


class GitHubConfig(TypedDict, total=False):
    permission: Required[Literal["pull", "push", "admin", "maintain", "triage"]]
    """Permission to grant on the repository."""

    target_id: Required[str]
    """Repository or organisation slug to grant access to."""


class DiscordConfig(TypedDict, total=False):
    guild_id: Required[str]
    """Discord guild (server) ID."""

    role_id: Optional[str]
    """Optional Discord role to assign within the guild."""


class TelegramConfig(TypedDict, total=False):
    chat_id: Required[str]
    """Telegram chat ID. For groups this is typically a negative integer."""


class FigmaConfig(TypedDict, total=False):
    figma_file_id: Required[str]
    """Figma file identifier to grant access to."""


class FramerConfig(TypedDict, total=False):
    framer_template_id: Required[str]
    """Framer template identifier to grant access to."""


class NotionConfig(TypedDict, total=False):
    notion_template_id: Required[str]
    """Notion template identifier to grant access to."""


class DigitalFilesConfig(TypedDict, total=False):
    digital_file_ids: Required[SequenceNotStr[str]]
    """Files attached to this entitlement.

    Add files via `POST /entitlements/{id}/files` and remove them via
    `DELETE /entitlements/{id}/files/{file_id}`.
    """

    external_url: Optional[str]
    """Optional external URL shown to the customer alongside the files."""

    instructions: Optional[str]
    """
    Optional human-readable delivery instructions shown to the customer alongside
    the files.
    """

    legacy_file_ids: Optional[SequenceNotStr[str]]
    """Three-way patchable list of legacy file identifiers:

    - omitted → preserve the current value
    - `null` → clear
    - `[...]` → replace

    On create, an omitted field, an explicit `null`, or an empty array all result in
    no legacy files attached.
    """


class LicenseKeyConfig(TypedDict, total=False):
    activation_message: Optional[str]
    """
    Optional message displayed when a customer activates the license key (≤ 2500
    characters).
    """

    activations_limit: Optional[int]
    """Maximum activations allowed per issued license key. Omit for unlimited."""

    duration_count: Optional[int]
    """Validity duration of issued license keys.

    Provide both `duration_count` and `duration_interval` together for a fixed
    duration; omit both for non-expiring keys.
    """

    duration_interval: Optional[TimeInterval]
    """Unit of `duration_count`."""


IntegrationConfigParam: TypeAlias = Union[
    GitHubConfig,
    DiscordConfig,
    TelegramConfig,
    FigmaConfig,
    FramerConfig,
    NotionConfig,
    DigitalFilesConfig,
    LicenseKeyConfig,
]
