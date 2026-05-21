# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .filter_operator import FilterOperator

__all__ = ["FilterType", "MeterFilterConditionList"]


class MeterFilterConditionList(BaseModel):
    key: str
    """Filter key to apply"""

    operator: FilterOperator
    """Filter operator"""

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


FilterType: TypeAlias = Union[List[MeterFilterConditionList], List["MeterFilter"]]

from .meter_filter import MeterFilter
