# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CancellationFeedback"]

CancellationFeedback: TypeAlias = Literal[
    "too_expensive",
    "missing_features",
    "switched_service",
    "unused",
    "customer_service",
    "low_quality",
    "too_complex",
    "other",
]
