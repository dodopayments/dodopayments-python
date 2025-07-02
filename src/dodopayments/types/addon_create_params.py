# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .tax_category import TaxCategory

__all__ = ["AddonCreateParams"]


class AddonCreateParams(TypedDict, total=False):
    currency: Required[Currency]
    """The currency of the Addon"""

    name: Required[str]
    """Name of the Addon"""

    price: Required[int]
    """Amount of the addon"""

    tax_category: Required[TaxCategory]
    """Tax category applied to this Addon"""

    description: Optional[str]
    """Optional description of the Addon"""
