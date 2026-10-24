# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .locale import Locale
from .metadata_param import MetadataParam

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    email: Optional[str]

    metadata: Optional[MetadataParam]
    """Additional metadata for the customer"""

    name: Optional[str]

    phone_number: Optional[str]

    preferred_locale: Optional[Locale]
    """The language of the customer emails, a code from `GET /locales`.

    A value replaces the current language, and `null` removes it. Send this field
    only to change the language on purpose. With no language, the emails are in
    English.
    """
