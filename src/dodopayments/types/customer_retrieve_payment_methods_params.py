# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .currency import Currency
from .country_code import CountryCode

__all__ = ["CustomerRetrievePaymentMethodsParams"]


class CustomerRetrievePaymentMethodsParams(TypedDict, total=False):
    billing_country: CountryCode
    """ISO country code alpha2 variant"""

    currency: Currency
