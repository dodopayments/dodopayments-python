# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .product_collections.product_collection_group_response import ProductCollectionGroupResponse

__all__ = ["ProductCollection"]


class ProductCollection(BaseModel):
    id: str
    """Unique identifier for the product collection"""

    brand_id: str
    """Brand ID for the collection"""

    created_at: datetime
    """Timestamp when the collection was created"""

    groups: List[ProductCollectionGroupResponse]
    """Groups in this collection"""

    name: str
    """Name of the collection"""

    updated_at: datetime
    """Timestamp when the collection was last updated"""

    description: Optional[str] = None
    """Description of the collection"""

    effective_at_on_downgrade: Optional[Literal["immediately", "next_billing_date"]] = None
    """
    Default effective_at setting for subscription plan downgrades (null = inherit
    from business)
    """

    effective_at_on_upgrade: Optional[Literal["immediately", "next_billing_date"]] = None
    """
    Default effective_at setting for subscription plan upgrades (null = inherit from
    business)
    """

    image: Optional[str] = None
    """URL of the collection image"""

    on_payment_failure: Optional[Literal["prevent_change", "apply_change"]] = None
    """
    Default behavior for subscription plan changes on payment failure (null =
    inherit from business)
    """

    proration_billing_mode_on_downgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ] = None
    """
    Default proration billing mode for subscription plan downgrades (null = inherit
    from business)
    """

    proration_billing_mode_on_upgrade: Optional[
        Literal["prorated_immediately", "full_immediately", "difference_immediately", "do_not_bill"]
    ] = None
    """
    Default proration billing mode for subscription plan upgrades (null = inherit
    from business)
    """
