# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["Product", "Price", "PriceOneTimePrice", "PriceRecurringPrice", "LicenseKeyDuration"]


class PriceOneTimePrice(BaseModel):
    currency: Literal[
        "AED",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BWP",
        "BYN",
        "BZD",
        "CAD",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SEK",
        "SGD",
        "SHP",
        "SLE",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STN",
        "SVC",
        "SZL",
        "THB",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
    ]

    discount: float
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    price: int
    """
    The payment amount, in the smallest denomination of the currency (e.g., cents
    for USD). For example, to charge $1.00, pass `100`.

    If [`pay_what_you_want`](Self::pay_what_you_want) is set to `true`, this field
    represents the **minimum** amount the customer must pay.
    """

    purchasing_power_parity: bool
    """
    Indicates if purchasing power parity adjustments are applied to the price.
    Purchasing power parity feature is not available as of now.
    """

    type: Literal["one_time_price"]

    pay_what_you_want: Optional[bool] = None
    """
    Indicates whether the customer can pay any amount they choose. If set to `true`,
    the [`price`](Self::price) field is the minimum amount.
    """

    suggested_price: Optional[int] = None
    """A suggested price for the user to pay.

    This value is only considered if [`pay_what_you_want`](Self::pay_what_you_want)
    is `true`. Otherwise, it is ignored.
    """

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive."""


class PriceRecurringPrice(BaseModel):
    currency: Literal[
        "AED",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BWP",
        "BYN",
        "BZD",
        "CAD",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "INR",
        "IQD",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SEK",
        "SGD",
        "SHP",
        "SLE",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STN",
        "SVC",
        "SZL",
        "THB",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
    ]

    discount: float
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    payment_frequency_count: int
    """
    Number of units for the payment frequency. For example, a value of `1` with a
    `payment_frequency_interval` of `month` represents monthly payments.
    """

    payment_frequency_interval: Literal["Day", "Week", "Month", "Year"]

    price: int
    """The payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    purchasing_power_parity: bool
    """
    Indicates if purchasing power parity adjustments are applied to the price.
    Purchasing power parity feature is not available as of now
    """

    subscription_period_count: int
    """
    Number of units for the subscription period. For example, a value of `12` with a
    `subscription_period_interval` of `month` represents a one-year subscription.
    """

    subscription_period_interval: Literal["Day", "Week", "Month", "Year"]

    type: Literal["recurring_price"]

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive"""

    trial_period_days: Optional[int] = None
    """Number of days for the trial period. A value of `0` indicates no trial period."""


Price: TypeAlias = Annotated[Union[PriceOneTimePrice, PriceRecurringPrice], PropertyInfo(discriminator="type")]


class LicenseKeyDuration(BaseModel):
    count: int

    interval: Literal["Day", "Week", "Month", "Year"]


class Product(BaseModel):
    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    license_key_enabled: bool
    """Indicates whether the product requires a license key."""

    price: Price

    product_id: str
    """Unique identifier for the product."""

    tax_category: Literal["digital_products", "saas", "e_book", "edtech"]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    updated_at: datetime
    """Timestamp when the product was last updated."""

    description: Optional[str] = None
    """Description of the product, optional."""

    image: Optional[str] = None
    """URL of the product image, optional."""

    license_key_activation_message: Optional[str] = None
    """Message sent upon license key activation, if applicable."""

    license_key_activations_limit: Optional[int] = None
    """Limit on the number of activations for the license key, if enabled."""

    license_key_duration: Optional[LicenseKeyDuration] = None

    name: Optional[str] = None
    """Name of the product, optional."""
