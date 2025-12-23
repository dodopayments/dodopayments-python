# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CheckoutSessionResponse"]


class CheckoutSessionResponse(BaseModel):
    session_id: str
    """The ID of the created checkout session"""

    checkout_url: Optional[str] = None
    """Checkout url (None when payment_method_id is provided)"""
