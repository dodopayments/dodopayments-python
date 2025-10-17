# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["NewCustomerParam"]


class NewCustomerParam(TypedDict, total=False):
    email: Required[str]
    """Email is required for creating a new customer"""

    name: Optional[str]
    """Optional full name of the customer.

    If provided during session creation, it is persisted and becomes immutable for
    the session. If omitted here, it can be provided later via the confirm API.
    """

    phone_number: Optional[str]
