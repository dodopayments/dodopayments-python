# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    collection_method: Literal["auto_charge", "manual"]

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    customer_id: str

    due_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    due_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    page_number: int
    """Page number. The default is 0."""

    page_size: int
    """Page size. The default is 10 and the maximum is 100."""

    status: List[Literal["open", "paid", "void", "draft", "past_due", "uncollectable"]]
    """
    Repeat the key to match more than one status, for example
    `status=open&status=past_due`.
    """

    subscription_id: str

    tags: List[Literal["refunded", "partially_refunded", "disputed", "payment_reversed"]]
    """Repeat the key to match an invoice that has any one of the tags."""

    total_amount_gte: int

    total_amount_lte: int
