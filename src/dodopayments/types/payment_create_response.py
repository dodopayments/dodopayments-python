# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

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

    payment_id: str

    total_amount: int

    payment_link: Optional[str] = None

    product_cart: Optional[List[ProductCart]] = None
