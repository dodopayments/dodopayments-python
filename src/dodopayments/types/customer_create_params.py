# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .locale import Locale
from .metadata_param import MetadataParam

__all__ = ["CustomerCreateParams"]


class CustomerCreateParams(TypedDict, total=False):
    email: Required[str]

    name: Required[str]

    metadata: MetadataParam
    """Additional metadata for the customer"""

    phone_number: Optional[str]

    preferred_locale: Optional[Locale]
    """The language of the customer emails, a code from `GET /locales`.

    With no value, the emails are in English until a checkout or the customer portal
    sets a language.
    """
