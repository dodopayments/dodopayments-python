# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .country_code import CountryCode

__all__ = ["BillingAddressParam"]


class BillingAddressParam(TypedDict, total=False):
    city: Required[str]
    """City name"""

    country: Required[CountryCode]
    """ISO country code alpha2 variant"""

    state: Required[str]
    """State or province name"""

    street: Required[str]
    """Street address including house number and unit/apartment if applicable"""

    zipcode: Required[str]
    """Postal code or ZIP code"""
