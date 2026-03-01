# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

from .conjunction import Conjunction
from .filter_operator import FilterOperator

__all__ = [
    "MeterFilterParam",
    "ClausesDirectFilterCondition",
    "ClausesNestedMeterFilter",
    "ClausesNestedMeterFilterClausesLevel1FilterCondition",
    "ClausesNestedMeterFilterClausesLevel1NestedFilter",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter",
    "ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause",
]


class ClausesDirectFilterCondition(TypedDict, total=False):
    """Filter condition with key, operator, and value"""

    key: Required[str]
    """Filter key to apply"""

    operator: Required[FilterOperator]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1FilterCondition(TypedDict, total=False):
    """Filter condition with key, operator, and value"""

    key: Required[str]
    """Filter key to apply"""

    operator: Required[FilterOperator]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition(TypedDict, total=False):
    """Filter condition with key, operator, and value"""

    key: Required[str]
    """Filter key to apply"""

    operator: Required[FilterOperator]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause(TypedDict, total=False):
    """Filter condition with key, operator, and value"""

    key: Required[str]
    """Filter key to apply"""

    operator: Required[FilterOperator]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter(TypedDict, total=False):
    """Level 3 nested filter (final nesting level)"""

    clauses: Required[Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause]]
    """Level 3: Filter conditions only (max depth reached)"""

    conjunction: Required[Conjunction]


class ClausesNestedMeterFilterClausesLevel1NestedFilter(TypedDict, total=False):
    """Level 2 nested filter"""

    clauses: Required[
        Union[
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition],
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter],
        ]
    ]
    """Level 2: Can be conditions or nested filters (1 more level allowed)"""

    conjunction: Required[Conjunction]


class ClausesNestedMeterFilter(TypedDict, total=False):
    """Level 1 nested filter - can contain Level 2 filters"""

    clauses: Required[
        Union[
            Iterable[ClausesNestedMeterFilterClausesLevel1FilterCondition],
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilter],
        ]
    ]
    """Level 1: Can be conditions or nested filters (2 more levels allowed)"""

    conjunction: Required[Conjunction]


class MeterFilterParam(TypedDict, total=False):
    """
    A filter structure that combines multiple conditions with logical conjunctions (AND/OR).

    Supports up to 3 levels of nesting to create complex filter expressions.
    Each filter has a conjunction (and/or) and clauses that can be either direct conditions or nested filters.
    """

    clauses: Required[Union[Iterable[ClausesDirectFilterCondition], Iterable[ClausesNestedMeterFilter]]]
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Required[Conjunction]
    """Logical conjunction to apply between clauses (and/or)"""
