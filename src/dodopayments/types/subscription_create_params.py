# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    billing: Required[BillingAddressParam]

    customer: Required[CustomerRequestParam]

    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    discount_code: Optional[str]
    """Discount Code to apply to the subscription"""

    metadata: Dict[str, str]

    payment_link: Optional[bool]
    """If true, generates a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """Optional URL to redirect after successful subscription creation"""

    tax_id: Optional[str]
    """Tax ID in case the payment is B2B.

    If tax id validation fails the payment creation will fail
    """

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """
