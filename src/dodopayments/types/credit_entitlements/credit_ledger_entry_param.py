# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditLedgerEntryParam"]


class CreditLedgerEntryParam(TypedDict, total=False):
    """Response for a ledger entry"""

    id: Required[str]

    amount: Required[str]

    balance_after: Required[str]

    balance_before: Required[str]

    business_id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    credit_entitlement_id: Required[str]

    customer_id: Required[str]

    is_credit: Required[bool]

    overage_after: Required[str]

    overage_before: Required[str]

    transaction_type: Required[
        Literal[
            "credit_added",
            "credit_deducted",
            "credit_expired",
            "credit_rolled_over",
            "rollover_forfeited",
            "overage_charged",
            "auto_top_up",
            "manual_adjustment",
            "refund",
        ]
    ]

    description: Optional[str]

    grant_id: Optional[str]

    reference_id: Optional[str]

    reference_type: Optional[str]
