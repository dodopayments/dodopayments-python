# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .addon_cart_response_item import AddonCartResponseItem
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["SubscriptionCreateResponse"]


class SubscriptionCreateResponse(BaseModel):
    addons: List[AddonCartResponseItem]
    """Addons associated with this subscription"""

    customer: CustomerLimitedDetails

    metadata: Dict[str, str]

    payment_id: str
    """First payment id for the subscription"""

    recurring_pre_tax_amount: int
    """
    Tax will be added to the amount and charged to the customer on each billing
    cycle
    """

    subscription_id: str
    """Unique identifier for the subscription"""

    client_secret: Optional[str] = None
    """
    Client secret used to load Dodo checkout SDK NOTE : Dodo checkout SDK will be
    coming soon
    """

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    payment_link: Optional[str] = None
    """URL to checkout page"""
