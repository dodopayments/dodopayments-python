# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .currency import Currency

__all__ = ["OnDemandSubscriptionParam"]


class OnDemandSubscriptionParam(TypedDict, total=False):
    mandate_only: Required[bool]
    """
    If set as True, does not perform any charge and only authorizes payment method
    details for future use.
    """

    adaptive_currency_fees_inclusive: Optional[bool]
    """
    Whether adaptive currency fees should be included in the product_price (true) or
    added on top (false). This field is ignored if adaptive pricing is not enabled
    for the business.
    """

    product_currency: Optional[Currency]
    """Optional currency of the product price.

    If not specified, defaults to the currency of the product.
    """

    product_description: Optional[str]
    """
    Optional product description override for billing and line items. If not
    specified, the stored description of the product will be used.
    """

    product_price: Optional[int]
    """
    Product price for the initial charge to customer If not specified the stored
    price of the product will be used Represented in the lowest denomination of the
    currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """
