# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .currency import Currency

__all__ = ["PaymentRetrieveLineItemsParams"]


class PaymentRetrieveLineItemsParams(TypedDict, total=False):
    currency: Currency
    """The currency of the amounts.

    It must be the currency that the customer paid in. Without it, the amounts are
    in the settlement currency.
    """
