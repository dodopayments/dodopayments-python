# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .currency import Currency
from .tax_category import TaxCategory

__all__ = ["AddonUpdateParams"]


class AddonUpdateParams(TypedDict, total=False):
    currency: Optional[Currency]
    """The currency of the Addon"""

    description: Optional[str]
    """Description of the Addon, optional and must be at most 1000 characters."""

    image_id: Optional[str]
    """Addon image id after its uploaded to S3"""

    name: Optional[str]
    """Name of the Addon, optional and must be at most 100 characters."""

    price: Optional[int]
    """Amount of the addon"""

    tax_category: Optional[TaxCategory]
    """Tax category of the Addon."""
