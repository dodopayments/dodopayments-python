# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["PaymentCreateResponse", "Customer", "ProductCart"]


class Customer(BaseModel):
    customer_id: str

    email: str

    name: str


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class PaymentCreateResponse(BaseModel):
    client_secret: str

    customer: Customer

    metadata: Dict[str, str]

    payment_id: str

    total_amount: int

    payment_link: Optional[str] = None

    product_cart: Optional[List[ProductCart]] = None
