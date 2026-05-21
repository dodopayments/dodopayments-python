# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CheckoutSessionResponse"]


class CheckoutSessionResponse(BaseModel):
    session_id: str
    """The ID of the created checkout session"""

    checkout_url: Optional[str] = None
    """Checkout url (None when payment_method_id is provided)"""

    client_secret: Optional[str] = None
    """Client secret used to load the Dodo Payments checkout SDK.

    Returned when `confirm: true` was passed and a PaymentIntent was created at
    session-creation time. `None` otherwise.
    """

    payment_id: Optional[str] = None
    """
    Underlying payment id when `confirm: true` was passed and a PaymentIntent was
    created at session-creation time. `None` otherwise.
    """

    publishable_key: Optional[str] = None
    """Publishable key for the Dodo Payments checkout SDK.

    Returned when `confirm: true` was passed and a PaymentIntent was created at
    session-creation time. `None` otherwise.
    """
