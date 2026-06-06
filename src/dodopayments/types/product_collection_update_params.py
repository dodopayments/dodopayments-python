# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductCollectionUpdateParams"]


class ProductCollectionUpdateParams(TypedDict, total=False):
    brand_id: Optional[str]
    """Optional brand_id update"""

    description: Optional[str]
    """Optional description update - pass null to remove, omit to keep unchanged"""

    effective_at_on_downgrade: Optional[Literal["immediately", "next_billing_date"]]
    """
    Effective_at setting for downgrades: Some(Some(val)) = set, Some(None) = clear
    (inherit), None = no change
    """

    effective_at_on_upgrade: Optional[Literal["immediately", "next_billing_date"]]
    """
    Effective_at setting for upgrades: Some(Some(val)) = set, Some(None) = clear
    (inherit), None = no change
    """

    group_order: Optional[SequenceNotStr[str]]
    """Optional new order for groups (array of group UUIDs in desired order)"""

    image_id: Optional[str]
    """Optional image update - pass null to remove, omit to keep unchanged"""

    name: Optional[str]
    """Optional new name for the collection"""

    on_payment_failure: Optional[Literal["prevent_change", "apply_change"]]
    """
    On payment failure behavior: Some(Some(val)) = set, Some(None) = clear
    (inherit), None = no change
    """

    proration_billing_mode_on_downgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ]
    """
    Proration billing mode for downgrades: Some(Some(val)) = set, Some(None) = clear
    (inherit), None = no change
    """

    proration_billing_mode_on_upgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ]
    """
    Proration billing mode for upgrades: Some(Some(val)) = set, Some(None) = clear
    (inherit), None = no change
    """
