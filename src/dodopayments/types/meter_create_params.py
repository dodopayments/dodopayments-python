# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .meter_filter_param import MeterFilterParam
from .meter_aggregation_param import MeterAggregationParam

__all__ = ["MeterCreateParams"]


class MeterCreateParams(TypedDict, total=False):
    aggregation: Required[MeterAggregationParam]
    """Aggregation configuration for the meter"""

    event_name: Required[str]
    """Event name to track"""

    measurement_unit: Required[str]
    """measurement unit"""

    name: Required[str]
    """Name of the meter"""

    description: Optional[str]
    """Optional description of the meter"""

    filter: Optional[MeterFilterParam]
    """Optional filter to apply to the meter"""
