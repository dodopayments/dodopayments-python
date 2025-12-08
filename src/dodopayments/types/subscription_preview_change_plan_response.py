# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .currency import Currency
from .subscription import Subscription
from .tax_category import TaxCategory

__all__ = [
    "SubscriptionPreviewChangePlanResponse",
    "ImmediateCharge",
    "ImmediateChargeLineItem",
    "ImmediateChargeLineItemUnionMember0",
    "ImmediateChargeLineItemUnionMember1",
    "ImmediateChargeLineItemUnionMember2",
    "ImmediateChargeSummary",
]


class ImmediateChargeLineItemUnionMember0(BaseModel):
    id: str

    currency: Currency

    product_id: str

    proration_factor: float

    quantity: int

    tax_inclusive: bool

    type: Literal["subscription"]

    unit_price: int

    description: Optional[str] = None

    name: Optional[str] = None

    tax: Optional[int] = None

    tax_rate: Optional[float] = None


class ImmediateChargeLineItemUnionMember1(BaseModel):
    id: str

    currency: Currency

    name: str

    proration_factor: float

    quantity: int

    tax_category: TaxCategory
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    tax_inclusive: bool

    tax_rate: float

    type: Literal["addon"]

    unit_price: int

    description: Optional[str] = None

    tax: Optional[int] = None


class ImmediateChargeLineItemUnionMember2(BaseModel):
    id: str

    chargeable_units: str

    currency: Currency

    free_threshold: int

    name: str

    price_per_unit: str

    subtotal: int

    tax_inclusive: bool

    tax_rate: float

    type: Literal["meter"]

    units_consumed: str

    description: Optional[str] = None

    tax: Optional[int] = None


ImmediateChargeLineItem: TypeAlias = Union[
    ImmediateChargeLineItemUnionMember0, ImmediateChargeLineItemUnionMember1, ImmediateChargeLineItemUnionMember2
]


class ImmediateChargeSummary(BaseModel):
    currency: Currency

    customer_credits: int

    settlement_amount: int

    settlement_currency: Currency

    total_amount: int

    settlement_tax: Optional[int] = None

    tax: Optional[int] = None


class ImmediateCharge(BaseModel):
    line_items: List[ImmediateChargeLineItem]

    summary: ImmediateChargeSummary


class SubscriptionPreviewChangePlanResponse(BaseModel):
    immediate_charge: ImmediateCharge

    new_plan: Subscription
    """Response struct representing subscription details"""
