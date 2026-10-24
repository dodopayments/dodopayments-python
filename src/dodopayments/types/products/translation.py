# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..locale import Locale
from ..._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    """
    The translation of a product, an add-on, a product collection or a meter in one locale.
    """

    locale: Locale
    """The locale of the translation."""

    updated_at: datetime
    """The time of the last change."""

    description: Optional[str] = None
    """The translated description.

    `null` shows that the description has no translation.
    """

    name: Optional[str] = None
    """The translated name. `null` shows that the name has no translation."""
