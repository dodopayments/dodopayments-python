# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MeterCreditEntitlementCartResponse"]


class MeterCreditEntitlementCartResponse(BaseModel):
    """
    Response struct representing meter-credit entitlement mapping cart details for a subscription
    """

    credit_entitlement_id: str

    meter_id: str

    meter_name: str

    meter_units_per_credit: str

    product_id: str
