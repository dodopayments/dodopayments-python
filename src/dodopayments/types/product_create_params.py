# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ProductCreateParams", "Price", "PriceOneTimePrice", "PriceRecurringPrice", "LicenseKeyDuration"]


class ProductCreateParams(TypedDict, total=False):
    price: Required[Price]

    tax_category: Required[Literal["digital_products", "saas", "e_book", "edtech"]]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    description: Optional[str]
    """Optional description of the product"""

    license_key_activation_message: Optional[str]
    """Optional message displayed during license key activation"""

    license_key_activations_limit: Optional[int]
    """The number of times the license key can be activated. Must be 0 or greater"""

    license_key_duration: Optional[LicenseKeyDuration]

    license_key_enabled: Optional[bool]
    """
    When true, generates and sends a license key to your customer. Defaults to false
    """

    name: Optional[str]
    """Optional name of the product"""


class PriceOneTimePrice(TypedDict, total=False):
    currency: Required[
        Literal[
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
    ]

    discount: Required[float]
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    price: Required[int]
    """
    The payment amount, in the smallest denomination of the currency (e.g., cents
    for USD). For example, to charge $1.00, pass `100`.

    If [`pay_what_you_want`](Self::pay_what_you_want) is set to `true`, this field
    represents the **minimum** amount the customer must pay.
    """

    purchasing_power_parity: Required[bool]
    """
    Indicates if purchasing power parity adjustments are applied to the price.
    Purchasing power parity feature is not available as of now.
    """

    type: Required[Literal["one_time_price"]]

    pay_what_you_want: bool
    """
    Indicates whether the customer can pay any amount they choose. If set to `true`,
    the [`price`](Self::price) field is the minimum amount.
    """

    suggested_price: Optional[int]
    """A suggested price for the user to pay.

    This value is only considered if [`pay_what_you_want`](Self::pay_what_you_want)
    is `true`. Otherwise, it is ignored.
    """

    tax_inclusive: Optional[bool]
    """Indicates if the price is tax inclusive."""


class PriceRecurringPrice(TypedDict, total=False):
    currency: Required[
        Literal[
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
    ]

    discount: Required[float]
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    payment_frequency_count: Required[int]
    """
    Number of units for the payment frequency. For example, a value of `1` with a
    `payment_frequency_interval` of `month` represents monthly payments.
    """

    payment_frequency_interval: Required[Literal["Day", "Week", "Month", "Year"]]

    price: Required[int]
    """The payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    purchasing_power_parity: Required[bool]
    """
    Indicates if purchasing power parity adjustments are applied to the price.
    Purchasing power parity feature is not available as of now
    """

    subscription_period_count: Required[int]
    """
    Number of units for the subscription period. For example, a value of `12` with a
    `subscription_period_interval` of `month` represents a one-year subscription.
    """

    subscription_period_interval: Required[Literal["Day", "Week", "Month", "Year"]]

    type: Required[Literal["recurring_price"]]

    tax_inclusive: Optional[bool]
    """Indicates if the price is tax inclusive"""

    trial_period_days: int
    """Number of days for the trial period. A value of `0` indicates no trial period."""


Price: TypeAlias = Union[PriceOneTimePrice, PriceRecurringPrice]


class LicenseKeyDuration(TypedDict, total=False):
    count: Required[int]

    interval: Required[Literal["Day", "Week", "Month", "Year"]]
