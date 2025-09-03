# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeterAggregation"]


class MeterAggregation(BaseModel):
    type: Literal["count", "sum", "max", "last"]
    """Aggregation type for the meter"""

    key: Optional[str] = None
    """Required when type is not COUNT"""
