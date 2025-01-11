# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["PaymentCreateResponse", "Customer", "ProductCart"]


class Customer(BaseModel):
    customer_id: str
    """Unique identifier for the customer"""

    email: str
    """Email address of the customer"""

    name: str
    """Full name of the customer"""


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class PaymentCreateResponse(BaseModel):
    client_secret: str
    """
    Client secret used to load Dodo checkout SDK NOTE : Dodo checkout SDK will be
    coming soon
    """

    customer: Customer

    metadata: Dict[str, str]

    payment_id: str
    """Unique identifier for the payment"""

    total_amount: int
    """Total amount of the payment in smallest currency unit (e.g. cents)"""

    payment_link: Optional[str] = None
    """Optional URL to a hosted payment page"""

    product_cart: Optional[List[ProductCart]] = None
    """Optional list of products included in the payment"""
