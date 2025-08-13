# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .subscription_status import SubscriptionStatus
from .billing_address_param import BillingAddressParam

__all__ = ["SubscriptionUpdateParams", "DisableOnDemand"]


class SubscriptionUpdateParams(TypedDict, total=False):
    billing: Optional[BillingAddressParam]

    cancel_at_next_billing_date: Optional[bool]

    disable_on_demand: Optional[DisableOnDemand]

    metadata: Optional[Dict[str, str]]

    next_billing_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    status: Optional[SubscriptionStatus]

    tax_id: Optional[str]


class DisableOnDemand(TypedDict, total=False):
    next_billing_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
