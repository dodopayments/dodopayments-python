# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MeterAggregationParam"]


class MeterAggregationParam(TypedDict, total=False):
    type: Required[Literal["count", "sum", "max", "last"]]
    """Aggregation type for the meter"""

    key: Optional[str]
    """Required when type is not COUNT"""
