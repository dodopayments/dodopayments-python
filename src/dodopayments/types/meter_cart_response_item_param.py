# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .currency import Currency

__all__ = ["MeterCartResponseItemParam"]


class MeterCartResponseItemParam(TypedDict, total=False):
    """Response struct representing usage-based meter cart details for a subscription"""

    currency: Required[Currency]

    free_threshold: Required[int]

    measurement_unit: Required[str]

    meter_id: Required[str]

    name: Required[str]

    description: Optional[str]

    price_per_unit: Optional[str]
