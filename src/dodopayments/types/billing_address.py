# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .country_code import CountryCode

__all__ = ["BillingAddress"]


class BillingAddress(BaseModel):
    country: CountryCode
    """Two-letter ISO country code (ISO 3166-1 alpha-2)"""

    city: Optional[str] = None
    """City name"""

    state: Optional[str] = None
    """State or province name"""

    street: Optional[str] = None
    """Street address including house number and unit/apartment if applicable"""

    zipcode: Optional[str] = None
    """Postal code or ZIP code"""
