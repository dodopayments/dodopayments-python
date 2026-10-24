# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..locale import Locale
from ..._models import BaseModel

__all__ = ["EntitlementTranslation"]


class EntitlementTranslation(BaseModel):
    """The translation of an entitlement in one locale."""

    locale: Locale
    """The locale of the translation."""

    updated_at: datetime
    """The time of the last change."""

    activation_message: Optional[str] = None
    """The translated activation message of a `license_key` entitlement."""

    description: Optional[str] = None
    """The translated description.

    `null` shows that the description has no translation.
    """

    instructions: Optional[str] = None
    """The translated delivery instructions of a `digital_files` entitlement."""

    name: Optional[str] = None
    """The translated name. `null` shows that the name has no translation."""
