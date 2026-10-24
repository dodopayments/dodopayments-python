# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locale import Locale
from .._models import BaseModel

__all__ = ["LocaleInfo"]


class LocaleInfo(BaseModel):
    """A locale that the checkout and the customer portal can show."""

    code: Locale
    """The code to send in the `locale` parameter."""

    name: str
    """The English name of the language."""

    native_name: str
    """The name of the language in that language."""
