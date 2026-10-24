# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..locale import Locale
from ..._models import BaseModel

__all__ = ["CreditEntitlementTranslation"]


class CreditEntitlementTranslation(BaseModel):
    """The translation of a credit entitlement in one locale."""

    locale: Locale
    """The locale of the translation."""

    updated_at: datetime
    """The time of the last change."""

    name: Optional[str] = None
    """The translated name. `null` shows that the name has no translation."""

    unit: Optional[str] = None
    """The translated unit. `null` shows that the unit has no translation."""
