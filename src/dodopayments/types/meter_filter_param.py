# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .conjunction import Conjunction

__all__ = ["MeterFilterParam"]


class MeterFilterParam(TypedDict, total=False):
    """
    A filter structure that combines multiple conditions with logical conjunctions (AND/OR).

    Supports up to 3 levels of nesting to create complex filter expressions.
    Each filter has a conjunction (and/or) and clauses that can be either direct conditions or nested filters.
    """

    clauses: Required["FilterTypeParam"]
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Required[Conjunction]
    """Logical conjunction to apply between clauses (and/or)"""


from .filter_type_param import FilterTypeParam
