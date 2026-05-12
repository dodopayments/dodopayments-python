# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .attach_addon_param import AttachAddonParam

__all__ = ["ProductItemReqParam", "CreditEntitlement"]


class CreditEntitlement(TypedDict, total=False):
    """
    Per-checkout-session override for a single credit entitlement attached to a product.
    """

    credit_entitlement_id: Required[str]
    """ID of the credit entitlement to override.

    Must already be attached to the product.
    """

    credits_amount: Required[str]
    """
    Number of credits to grant for this checkout session, overriding the
    product-level `credits_amount` set on the credit entitlement mapping. Must be
    greater than zero.
    """


class ProductItemReqParam(TypedDict, total=False):
    product_id: Required[str]
    """unique id of the product"""

    quantity: Required[int]

    addons: Optional[Iterable[AttachAddonParam]]
    """only valid if product is a subscription"""

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored Represented in the lowest denomination
    of the currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    Only applicable for one time payments

    If amount is not set for pay_what_you_want product, customer is allowed to
    select the amount.
    """

    credit_entitlements: Optional[Iterable[CreditEntitlement]]
    """
    Per-checkout-session overrides for credit entitlements already attached to this
    product. Each entry overrides the `credits_amount` granted by the referenced
    credit entitlement when this checkout session is fulfilled. The
    credit_entitlement_id must already be attached to the product.
    """
