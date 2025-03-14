# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CreateNewCustomerParam"]


class CreateNewCustomerParam(TypedDict, total=False):
    email: Required[str]

    name: Required[str]

    create_new_customer: bool
    """
    When false, the most recently created customer object with the given email is
    used if exists. When true, a new customer object is always created False by
    default
    """

    phone_number: Optional[str]
