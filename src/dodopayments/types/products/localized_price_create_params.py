# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..currency import Currency
from ..country_code import CountryCode

__all__ = ["LocalizedPriceCreateParams"]


class LocalizedPriceCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount in the smallest currency unit (e.g., cents). Must be greater than zero."""

    currency: Required[Currency]
    """Currency to charge in. Must be a supported currency."""

    country_code: Optional[CountryCode]
    """
    Required when the product's pricing_mode is by_country; forbidden when
    by_currency.
    """
