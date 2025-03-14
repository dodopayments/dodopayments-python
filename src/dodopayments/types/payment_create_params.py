# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam
from .one_time_product_cart_item_param import OneTimeProductCartItemParam

__all__ = ["PaymentCreateParams"]


class PaymentCreateParams(TypedDict, total=False):
    billing: Required[BillingAddressParam]

    customer: Required[CustomerRequestParam]

    product_cart: Required[Iterable[OneTimeProductCartItemParam]]
    """List of products in the cart. Must contain at least 1 and at most 100 items."""

    discount_code: Optional[str]
    """Discount Code to apply to the transaction"""

    metadata: Dict[str, str]

    payment_link: Optional[bool]
    """Whether to generate a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """
    Optional URL to redirect the customer after payment. Must be a valid URL if
    provided.
    """

    tax_id: Optional[str]
    """Tax ID in case the payment is B2B.

    If tax id validation fails the payment creation will fail
    """
