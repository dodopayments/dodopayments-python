# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .country_code import CountryCode

__all__ = ["BillingAddress"]


class BillingAddress(BaseModel):
    city: str
    """City name"""

    country: CountryCode
    """Two-letter ISO country code (ISO 3166-1 alpha-2)"""

    state: str
    """State or province name"""

    street: str
    """Street address including house number and unit/apartment if applicable"""

    zipcode: str
    """Postal code or ZIP code"""
