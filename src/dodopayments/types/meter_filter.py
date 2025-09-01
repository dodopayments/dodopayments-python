# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MeterFilter",
    "ClausesDirectFilterCondition",
    "ClausesNestedMeterFilter",
    "ClausesNestedMeterFilterClausesLevel1FilterCondition",
    "ClausesNestedMeterFilterClausesLevel1NestedFilter",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause",
]


class ClausesDirectFilterCondition(BaseModel):
    key: str
    """Filter key to apply"""

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "greater_than_or_equals",
        "less_than",
        "less_than_or_equals",
        "contains",
        "does_not_contain",
    ]

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1FilterCondition(BaseModel):
    key: str
    """Filter key to apply"""

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "greater_than_or_equals",
        "less_than",
        "less_than_or_equals",
        "contains",
        "does_not_contain",
    ]

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition(BaseModel):
    key: str
    """Filter key to apply"""

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "greater_than_or_equals",
        "less_than",
        "less_than_or_equals",
        "contains",
        "does_not_contain",
    ]

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause(BaseModel):
    key: str
    """Filter key to apply"""

    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "greater_than_or_equals",
        "less_than",
        "less_than_or_equals",
        "contains",
        "does_not_contain",
    ]

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter(BaseModel):
    clauses: List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause]
    """Level 3: Filter conditions only (max depth reached)"""

    conjunction: Literal["and", "or"]


class ClausesNestedMeterFilterClausesLevel1NestedFilter(BaseModel):
    clauses: Union[
        List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition],
        List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter],
    ]
    """Level 2: Can be conditions or nested filters (1 more level allowed)"""

    conjunction: Literal["and", "or"]


class ClausesNestedMeterFilter(BaseModel):
    clauses: Union[
        List[ClausesNestedMeterFilterClausesLevel1FilterCondition],
        List[ClausesNestedMeterFilterClausesLevel1NestedFilter],
    ]
    """Level 1: Can be conditions or nested filters (2 more levels allowed)"""

    conjunction: Literal["and", "or"]


class MeterFilter(BaseModel):
    clauses: Union[List[ClausesDirectFilterCondition], List[ClausesNestedMeterFilter]]
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Literal["and", "or"]
    """Logical conjunction to apply between clauses (and/or)"""
