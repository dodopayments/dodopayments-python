# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .customer_limited_details import CustomerLimitedDetails
from .one_time_product_cart_item import OneTimeProductCartItem

__all__ = ["PaymentCreateResponse"]


class PaymentCreateResponse(BaseModel):
    client_secret: str
    """
    Client secret used to load Dodo checkout SDK NOTE : Dodo checkout SDK will be
    coming soon
    """

    customer: CustomerLimitedDetails
    """Limited details about the customer making the payment"""

    metadata: Dict[str, str]
    """Additional metadata associated with the payment"""

    payment_id: str
    """Unique identifier for the payment"""

    total_amount: int
    """Total amount of the payment in smallest currency unit (e.g. cents)"""

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    expires_on: Optional[datetime] = None
    """Expiry timestamp of the payment link"""

    payment_link: Optional[str] = None
    """Optional URL to a hosted payment page"""

    product_cart: Optional[List[OneTimeProductCartItem]] = None
    """Optional list of products included in the payment"""
