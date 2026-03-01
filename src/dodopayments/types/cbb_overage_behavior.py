# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CbbOverageBehavior"]

CbbOverageBehavior: TypeAlias = Literal[
    "forgive_at_reset", "invoice_at_billing", "carry_deficit", "carry_deficit_auto_repay"
]
