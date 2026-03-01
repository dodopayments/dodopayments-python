# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel
from .conjunction import Conjunction
from .filter_operator import FilterOperator

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
    """Filter condition with key, operator, and value"""

    key: str
    """Filter key to apply"""

    operator: FilterOperator

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1FilterCondition(BaseModel):
    """Filter condition with key, operator, and value"""

    key: str
    """Filter key to apply"""

    operator: FilterOperator

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition(BaseModel):
    """Filter condition with key, operator, and value"""

    key: str
    """Filter key to apply"""

    operator: FilterOperator

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause(BaseModel):
    """Filter condition with key, operator, and value"""

    key: str
    """Filter key to apply"""

    operator: FilterOperator

    value: Union[str, float, bool]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter(BaseModel):
    """Level 3 nested filter (final nesting level)"""

    clauses: List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause]
    """Level 3: Filter conditions only (max depth reached)"""

    conjunction: Conjunction


class ClausesNestedMeterFilterClausesLevel1NestedFilter(BaseModel):
    """Level 2 nested filter"""

    clauses: Union[
        List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition],
        List[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter],
    ]
    """Level 2: Can be conditions or nested filters (1 more level allowed)"""

    conjunction: Conjunction


class ClausesNestedMeterFilter(BaseModel):
    """Level 1 nested filter - can contain Level 2 filters"""

    clauses: Union[
        List[ClausesNestedMeterFilterClausesLevel1FilterCondition],
        List[ClausesNestedMeterFilterClausesLevel1NestedFilter],
    ]
    """Level 1: Can be conditions or nested filters (2 more levels allowed)"""

    conjunction: Conjunction


class MeterFilter(BaseModel):
    """
    A filter structure that combines multiple conditions with logical conjunctions (AND/OR).

    Supports up to 3 levels of nesting to create complex filter expressions.
    Each filter has a conjunction (and/or) and clauses that can be either direct conditions or nested filters.
    """

    clauses: Union[List[ClausesDirectFilterCondition], List[ClausesNestedMeterFilter]]
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Conjunction
    """Logical conjunction to apply between clauses (and/or)"""
