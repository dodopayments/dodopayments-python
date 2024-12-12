# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeParam"]


class DisputeParam(TypedDict, total=False):
    amount: Required[str]

    business_id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    currency: Required[str]

    dispute_id: Required[str]

    dispute_stage: Required[Literal["pre_dispute", "dispute", "pre_arbitration"]]

    dispute_status: Required[
        Literal[
            "dispute_opened",
            "dispute_expired",
            "dispute_accepted",
            "dispute_cancelled",
            "dispute_challenged",
            "dispute_won",
            "dispute_lost",
        ]
    ]

    payment_id: Required[str]
