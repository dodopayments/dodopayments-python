# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .conjunction import Conjunction

__all__ = ["MeterFilter"]


class MeterFilter(BaseModel):
    """
    A filter structure that combines multiple conditions with logical conjunctions (AND/OR).

    Supports up to 3 levels of nesting to create complex filter expressions.
    Each filter has a conjunction (and/or) and clauses that can be either direct conditions or nested filters.
    """

    clauses: "FilterType"
    """
    Filter clauses - can be direct conditions or nested filters (up to 3 levels
    deep)
    """

    conjunction: Conjunction
    """Logical conjunction to apply between clauses (and/or)"""


from .filter_type import FilterType
