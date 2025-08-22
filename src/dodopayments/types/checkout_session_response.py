# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CheckoutSessionResponse"]


class CheckoutSessionResponse(BaseModel):
    checkout_url: str
    """Checkout url"""

    session_id: str
    """The ID of the created checkout session"""
