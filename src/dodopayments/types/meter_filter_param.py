# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

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
    key: Required[str]
    """Filter key to apply"""

    operator: Required[
        Literal[
            "equals",
            "not_equals",
            "greater_than",
            "greater_than_or_equals",
            "less_than",
            "less_than_or_equals",
            "contains",
            "does_not_contain",
        ]
    ]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1FilterCondition(TypedDict, total=False):
    key: Required[str]
    """Filter key to apply"""

    operator: Required[
        Literal[
            "equals",
            "not_equals",
            "greater_than",
            "greater_than_or_equals",
            "less_than",
            "less_than_or_equals",
            "contains",
            "does_not_contain",
        ]
    ]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition(TypedDict, total=False):
    key: Required[str]
    """Filter key to apply"""

    operator: Required[
        Literal[
            "equals",
            "not_equals",
            "greater_than",
            "greater_than_or_equals",
            "less_than",
            "less_than_or_equals",
            "contains",
            "does_not_contain",
        ]
    ]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause(TypedDict, total=False):
    key: Required[str]
    """Filter key to apply"""

    operator: Required[
        Literal[
            "equals",
            "not_equals",
            "greater_than",
            "greater_than_or_equals",
            "less_than",
            "less_than_or_equals",
            "contains",
            "does_not_contain",
        ]
    ]

    value: Required[Union[str, float, bool]]
    """Filter value - can be string, number, or boolean"""


class ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter(TypedDict, total=False):
    clauses: Required[Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilterClause]]
    """Level 3: Filter conditions only (max depth reached)"""

    conjunction: Required[Literal["and", "or"]]


class ClausesNestedMeterFilterClausesLevel1NestedFilter(TypedDict, total=False):
    clauses: Required[
        Union[
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2FilterCondition],
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilterClausesLevel2NestedFilter],
        ]
    ]
    """Level 2: Can be conditions or nested filters (1 more level allowed)"""

    conjunction: Required[Literal["and", "or"]]


class ClausesNestedMeterFilter(TypedDict, total=False):
    clauses: Required[
        Union[
            Iterable[ClausesNestedMeterFilterClausesLevel1FilterCondition],
            Iterable[ClausesNestedMeterFilterClausesLevel1NestedFilter],
        ]
    ]
    """Level 1: Can be conditions or nested filters (2 more levels allowed)"""

    conjunction: Required[Literal["and", "or"]]


class MeterFilterParam(TypedDict, total=False):
    clauses: Required[Union[Iterable[ClausesDirectFilterCondition], Iterable[ClausesNestedMeterFilter]]]
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Required[Literal["and", "or"]]
    """Logical conjunction to apply between clauses (and/or)"""
