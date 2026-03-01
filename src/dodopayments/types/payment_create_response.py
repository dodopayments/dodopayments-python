# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["PaymentCreateResponse", "ProductCart"]


class ProductCart(BaseModel):
    product_id: str

    quantity: int

    amount: Optional[int] = None
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored Represented in the lowest denomination
    of the currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """


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

    product_cart: Optional[List[ProductCart]] = None
    """Optional list of products included in the payment"""
