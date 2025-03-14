# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DisputeStatus"]

DisputeStatus: TypeAlias = Literal[
    "dispute_opened",
    "dispute_expired",
    "dispute_accepted",
    "dispute_cancelled",
    "dispute_challenged",
    "dispute_won",
    "dispute_lost",
]
