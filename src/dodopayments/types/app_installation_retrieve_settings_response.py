# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AppInstallationRetrieveSettingsResponse"]


class AppInstallationRetrieveSettingsResponse(BaseModel):
    """The settings of the App Installation of the app token, with the secret values."""

    action_needed: bool
    """`true` when a required field has no value, or a stored value fails a live rule."""

    app_id: str

    installation_id: str

    invalid_keys: List[str]
    """The keys that need an action."""

    secrets: object
    """The values of the secret fields of the live manifest, by key."""

    values: object
    """The values of the fields of the live manifest that are not secrets."""

    live_manifest_version: Optional[int] = None
    """The version of the live settings manifest.

    It is `null` when the app has no live manifest. Then `values` and `secrets` are
    empty.
    """

    manifest_version: Optional[int] = None
    """The manifest version of the last save.

    It is `null` when the installation has no settings.
    """

    updated_at: Optional[datetime] = None
    """The time of the last save."""
