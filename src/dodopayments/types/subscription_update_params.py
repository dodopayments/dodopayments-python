# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .subscription_status import SubscriptionStatus
from .billing_address_param import BillingAddressParam

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    billing: Optional[BillingAddressParam]

    metadata: Optional[Dict[str, str]]

    status: Optional[SubscriptionStatus]

    tax_id: Optional[str]
