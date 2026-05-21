# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..group_product_param import GroupProductParam

__all__ = ["ItemCreateParams"]


class ItemCreateParams(TypedDict, total=False):
    id: Required[str]

    products: Required[Iterable[GroupProductParam]]
    """Products to add to the group"""
