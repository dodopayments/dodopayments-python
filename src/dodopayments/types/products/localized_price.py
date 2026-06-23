# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..currency import Currency
from .pricing_mode import PricingMode
from ..country_code import CountryCode

__all__ = ["LocalizedPrice"]


class LocalizedPrice(BaseModel):
    id: str
    """Unique identifier for the localized price."""

    amount: int
    """Amount in the smallest currency unit (e.g., cents)."""

    created_at: datetime
    """Timestamp when the localized price was created."""

    currency: Currency
    """Currency to charge in."""

    mode: PricingMode
    """Pricing mode of the rule: by_currency or by_country."""

    product_id: str
    """Product this localized price belongs to."""

    updated_at: datetime
    """Timestamp when the localized price was last updated."""

    country_code: Optional[CountryCode] = None
    """Country the rule applies to. Only set when mode is by_country."""
