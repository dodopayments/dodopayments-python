# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceUpdateDunningParams"]


class InvoiceUpdateDunningParams(TypedDict, total=False):
    action: Required[Literal["pause", "resume", "reschedule"]]

    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    offsets_days: Optional[Iterable[int]]
    """Needed for `reschedule`. Days from the due date."""
