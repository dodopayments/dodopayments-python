# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RefundCreateParams", "Item"]


class RefundCreateParams(TypedDict, total=False):
    payment_id: Required[str]
    """The unique identifier of the payment to be refunded."""

    items: Optional[Iterable[Item]]
    """Partially Refund an Individual Item"""

    metadata: Dict[str, str]
    """Additional metadata associated with the refund."""

    reason: Optional[str]
    """The reason for the refund, if any. Maximum length is 3000 characters. Optional."""


class Item(TypedDict, total=False):
    item_id: Required[str]
    """The id of the item (i.e. `product_id` or `addon_id`)"""

    amount: Optional[int]
    """The amount to refund. if None the whole item is refunded"""

    tax_inclusive: bool
    """Specify if tax is inclusive of the refund. Default true."""
