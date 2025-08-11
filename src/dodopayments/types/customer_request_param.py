# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .new_customer_param import NewCustomerParam
from .attach_existing_customer_param import AttachExistingCustomerParam

__all__ = ["CustomerRequestParam"]

CustomerRequestParam: TypeAlias = Union[AttachExistingCustomerParam, NewCustomerParam]
