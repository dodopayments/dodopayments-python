# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OneTimeProductCartItem"]


class OneTimeProductCartItem(BaseModel):
    product_id: str

    quantity: int
