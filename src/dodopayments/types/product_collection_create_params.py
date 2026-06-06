# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .product_collections.product_collection_group_details_param import ProductCollectionGroupDetailsParam

__all__ = ["ProductCollectionCreateParams"]


class ProductCollectionCreateParams(TypedDict, total=False):
    groups: Required[Iterable[ProductCollectionGroupDetailsParam]]
    """Groups of products in this collection"""

    name: Required[str]
    """Name of the product collection"""

    brand_id: Optional[str]
    """Brand id for the collection, if not provided will default to primary brand"""

    description: Optional[str]
    """Optional description of the product collection"""

    effective_at_on_downgrade: Optional[Literal["immediately", "next_billing_date"]]
    """
    Default effective_at setting for subscription plan downgrades (NULL = inherit
    from business)
    """

    effective_at_on_upgrade: Optional[Literal["immediately", "next_billing_date"]]
    """
    Default effective_at setting for subscription plan upgrades (NULL = inherit from
    business)
    """

    on_payment_failure: Optional[Literal["prevent_change", "apply_change"]]
    """
    Default behavior for subscription plan changes on payment failure (NULL =
    inherit from business)
    """

    proration_billing_mode_on_downgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ]
    """
    Default proration billing mode for subscription plan downgrades (NULL = inherit
    from business)
    """

    proration_billing_mode_on_upgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ]
    """
    Default proration billing mode for subscription plan upgrades (NULL = inherit
    from business)
    """
