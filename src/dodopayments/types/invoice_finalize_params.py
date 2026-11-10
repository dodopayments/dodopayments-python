# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["InvoiceFinalizeParams"]


class InvoiceFinalizeParams(TypedDict, total=False):
    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    cc_emails: Optional[SequenceNotStr[str]]
    """10 addresses or fewer."""

    customer_email: Optional[str]

    send: bool
    """`true` sends the invoice email after finalise."""
