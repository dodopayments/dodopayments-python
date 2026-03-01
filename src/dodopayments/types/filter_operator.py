# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FilterOperator"]

FilterOperator: TypeAlias = Literal[
    "equals",
    "not_equals",
    "greater_than",
    "greater_than_or_equals",
    "less_than",
    "less_than_or_equals",
    "contains",
    "does_not_contain",
]
