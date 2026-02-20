# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .currency import Currency
from .country_code import CountryCode
from .tax_category import TaxCategory

__all__ = [
    "CheckoutSessionPreviewResponse",
    "CurrentBreakup",
    "ProductCart",
    "ProductCartCreditEntitlement",
    "ProductCartMeter",
    "ProductCartAddon",
    "RecurringBreakup",
]


class CurrentBreakup(BaseModel):
    """Breakup of the current payment"""

    discount: int
    """Total discount amount"""

    subtotal: int
    """Subtotal before discount (pre-tax original prices)"""

    total_amount: int
    """Total amount to be charged (final amount after all calculations)"""

    tax: Optional[int] = None
    """Total tax amount"""


class ProductCartCreditEntitlement(BaseModel):
    """
    Minimal credit entitlement info shown at checkout — what credits the customer will receive
    """

    credit_entitlement_id: str
    """ID of the credit entitlement"""

    credit_entitlement_name: str
    """Name of the credit entitlement"""

    credit_entitlement_unit: str
    """Unit label (e.g. "API Calls", "Tokens")"""

    credits_amount: str
    """Number of credits granted"""


class ProductCartMeter(BaseModel):
    measurement_unit: str

    name: str

    price_per_unit: str

    description: Optional[str] = None

    free_threshold: Optional[int] = None


class ProductCartAddon(BaseModel):
    addon_id: str

    currency: Currency

    discounted_price: int

    name: str

    og_currency: Currency

    og_price: int

    quantity: int

    tax_category: TaxCategory
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    tax_inclusive: bool

    tax_rate: int

    description: Optional[str] = None

    discount_amount: Optional[int] = None

    tax: Optional[int] = None


class ProductCart(BaseModel):
    credit_entitlements: List[ProductCartCreditEntitlement]
    """Credit entitlements that will be granted upon purchase"""

    currency: Currency
    """the currency in which the calculatiosn were made"""

    discounted_price: int
    """discounted price"""

    is_subscription: bool
    """Whether this is a subscription product (affects tax calculation in breakup)"""

    is_usage_based: bool

    meters: List[ProductCartMeter]

    og_currency: Currency
    """the product currency"""

    og_price: int
    """original price of the product"""

    product_id: str
    """unique id of the product"""

    quantity: int
    """Quanitity"""

    tax_category: TaxCategory
    """tax category"""

    tax_inclusive: bool
    """Whether tax is included in the price"""

    tax_rate: int
    """tax rate"""

    addons: Optional[List[ProductCartAddon]] = None

    description: Optional[str] = None

    discount_amount: Optional[int] = None
    """discount percentage"""

    discount_cycle: Optional[int] = None
    """number of cycles the discount will apply"""

    name: Optional[str] = None
    """name of the product"""

    tax: Optional[int] = None
    """total tax"""


class RecurringBreakup(BaseModel):
    """Breakup of recurring payments (None for one-time only)"""

    discount: int
    """Total discount amount"""

    subtotal: int
    """Subtotal before discount (pre-tax original prices)"""

    total_amount: int
    """Total recurring amount including tax"""

    tax: Optional[int] = None
    """Total tax on recurring payments"""


class CheckoutSessionPreviewResponse(BaseModel):
    """Data returned by the calculate checkout session API"""

    billing_country: CountryCode
    """Billing country"""

    currency: Currency
    """Currency in which the calculations were made"""

    current_breakup: CurrentBreakup
    """Breakup of the current payment"""

    product_cart: List[ProductCart]
    """The total product cart"""

    total_price: int
    """Total calculate price of the product cart"""

    recurring_breakup: Optional[RecurringBreakup] = None
    """Breakup of recurring payments (None for one-time only)"""

    tax_id_err_msg: Optional[str] = None
    """Error message if tax ID validation failed"""

    total_tax: Optional[int] = None
    """Total tax"""
