# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LocalizedPriceUpdateParams"]


class LocalizedPriceUpdateParams(TypedDict, total=False):
    product_id: Required[str]

    amount: Optional[int]
    """New amount in the smallest currency unit (e.g., cents).

    Must be greater than zero. The currency and country_code of an existing rule
    cannot be changed.
    """
