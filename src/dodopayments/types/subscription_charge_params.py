# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .currency import Currency

__all__ = ["SubscriptionChargeParams", "CustomerBalanceConfig"]


class SubscriptionChargeParams(TypedDict, total=False):
    product_price: Required[int]
    """The product price.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    adaptive_currency_fees_inclusive: Optional[bool]
    """
    Whether adaptive currency fees should be included in the product_price (true) or
    added on top (false). This field is ignored if adaptive pricing is not enabled
    for the business.
    """

    customer_balance_config: Optional[CustomerBalanceConfig]
    """Specify how customer balance is used for the payment"""

    metadata: Optional[Dict[str, str]]
    """Metadata for the payment.

    If not passed, the metadata of the subscription will be taken
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


class CustomerBalanceConfig(TypedDict, total=False):
    """Specify how customer balance is used for the payment"""

    allow_customer_credits_purchase: Optional[bool]
    """Allows Customer Credit to be purchased to settle payments"""

    allow_customer_credits_usage: Optional[bool]
    """Allows Customer Credit Balance to be used to settle payments"""
