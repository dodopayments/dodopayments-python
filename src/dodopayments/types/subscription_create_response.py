# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .addon_cart_response_item import AddonCartResponseItem
from .customer_limited_details import CustomerLimitedDetails
from .one_time_product_cart_item import OneTimeProductCartItem

__all__ = ["SubscriptionCreateResponse"]


class SubscriptionCreateResponse(BaseModel):
    addons: List[AddonCartResponseItem]
    """Addons associated with this subscription"""

    customer: CustomerLimitedDetails
    """Customer details associated with this subscription"""

    metadata: Dict[str, str]
    """Additional metadata associated with the subscription"""

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

    expires_on: Optional[datetime] = None
    """Expiry timestamp of the payment link"""

    one_time_product_cart: Optional[List[OneTimeProductCartItem]] = None
    """One time products associated with the purchase of subscription"""

    payment_link: Optional[str] = None
    """URL to checkout page"""
