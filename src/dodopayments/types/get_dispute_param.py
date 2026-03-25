# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .dispute_stage import DisputeStage
from .dispute_status import DisputeStatus
from .customer_limited_details_param import CustomerLimitedDetailsParam

__all__ = ["GetDisputeParam"]


class GetDisputeParam(TypedDict, total=False):
    amount: Required[str]
    """
    The amount involved in the dispute, represented as a string to accommodate
    precision.
    """

    business_id: Required[str]
    """The unique identifier of the business involved in the dispute."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp of when the dispute was created, in UTC."""

    currency: Required[str]
    """The currency of the disputed amount, represented as an ISO 4217 currency code."""

    customer: Required[CustomerLimitedDetailsParam]
    """The customer who filed the dispute"""

    dispute_id: Required[str]
    """The unique identifier of the dispute."""

    dispute_stage: Required[DisputeStage]
    """The current stage of the dispute process."""

    dispute_status: Required[DisputeStatus]
    """The current status of the dispute."""

    payment_id: Required[str]
    """The unique identifier of the payment associated with the dispute."""

    reason: Optional[str]
    """Reason for the dispute"""

    remarks: Optional[str]
    """Remarks"""
