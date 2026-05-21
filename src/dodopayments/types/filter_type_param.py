# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .filter_operator import FilterOperator

__all__ = ["FilterTypeParam", "MeterFilterConditionList"]


class MeterFilterConditionList(TypedDict, total=False):
    key: Required[str]
    """Filter key to apply"""

    operator: Required[FilterOperator]
    """Filter operator"""

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


FilterTypeParam: TypeAlias = Union[Iterable[MeterFilterConditionList], Iterable["MeterFilterParam"]]

from .meter_filter_param import MeterFilterParam
