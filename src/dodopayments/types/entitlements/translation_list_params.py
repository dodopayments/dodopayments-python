# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["TranslationListParams"]


class TranslationListParams(TypedDict, total=False):
    locale: SequenceNotStr[str]
    """Returns only these locales, for example `?locale=fr&locale=de`.

    With no value, the response has all the locales.
    """
