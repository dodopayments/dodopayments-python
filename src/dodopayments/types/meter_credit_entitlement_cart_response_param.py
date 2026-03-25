# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MeterCreditEntitlementCartResponseParam"]


class MeterCreditEntitlementCartResponseParam(TypedDict, total=False):
    """
    Response struct representing meter-credit entitlement mapping cart details for a subscription
    """

    credit_entitlement_id: Required[str]

    meter_id: Required[str]

    meter_name: Required[str]

    meter_units_per_credit: Required[str]

    product_id: Required[str]
