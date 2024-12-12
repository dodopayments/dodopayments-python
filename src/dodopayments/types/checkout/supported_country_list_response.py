# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .country_code_alpha2 import CountryCodeAlpha2

__all__ = ["SupportedCountryListResponse"]

SupportedCountryListResponse: TypeAlias = List[CountryCodeAlpha2]
