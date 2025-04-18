# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam

__all__ = ["SubscriptionCreateParams", "OnDemand"]


class SubscriptionCreateParams(TypedDict, total=False):
    billing: Required[BillingAddressParam]

    customer: Required[CustomerRequestParam]

    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    allowed_payment_method_types: Optional[
        List[
            Literal[
                "credit",
                "debit",
                "upi_collect",
                "upi_intent",
                "apple_pay",
                "cashapp",
                "google_pay",
                "multibanco",
                "bancontact_card",
                "eps",
                "ideal",
                "przelewy24",
                "affirm",
                "klarna",
                "sepa",
                "ach",
                "amazon_pay",
                "afterpay_clearpay",
            ]
        ]
    ]
    """List of payment methods allowed during checkout.

    Customers will **never** see payment methods that are **not** in this list.
    However, adding a method here **does not guarantee** customers will see it.
    Availability still depends on other factors (e.g., customer location, merchant
    settings).
    """

    billing_currency: Optional[
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

    discount_code: Optional[str]
    """Discount Code to apply to the subscription"""

    metadata: Dict[str, str]

    on_demand: Optional[OnDemand]

    payment_link: Optional[bool]
    """If true, generates a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """Optional URL to redirect after successful subscription creation"""

    show_saved_payment_methods: bool
    """Display saved payment methods of a returning customer False by default"""

    tax_id: Optional[str]
    """Tax ID in case the payment is B2B.

    If tax id validation fails the payment creation will fail
    """

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """


class OnDemand(TypedDict, total=False):
    mandate_only: Required[bool]
    """
    If set as True, does not perform any charge and only authorizes payment method
    details for future use.
    """

    product_price: Optional[int]
    """
    Product price for the initial charge to customer If not specified the stored
    price of the product will be used Represented in the lowest denomination of the
    currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """
