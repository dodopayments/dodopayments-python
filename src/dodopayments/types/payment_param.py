# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .refund_param import RefundParam
from .dispute_param import DisputeParam

__all__ = ["PaymentParam", "Customer", "ProductCart"]


class Customer(TypedDict, total=False):
    customer_id: Required[str]

    email: Required[str]

    name: Required[str]


class ProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]


class PaymentParam(TypedDict, total=False):
    business_id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

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

    customer: Required[Customer]

    disputes: Required[Iterable[DisputeParam]]

    payment_id: Required[str]

    refunds: Required[Iterable[RefundParam]]

    total_amount: Required[int]
    """Total amount taken from the customer including tax"""

    payment_link: Optional[str]

    payment_method: Optional[str]

    payment_method_type: Optional[str]

    product_cart: Optional[Iterable[ProductCart]]
    """Product Cart of One time payment.

    In case of subscription/recurring payment product id and quantity are available
    in Get Subscription Api
    """

    status: Optional[
        Literal[
            "succeeded",
            "failed",
            "cancelled",
            "processing",
            "requires_customer_action",
            "requires_merchant_action",
            "requires_payment_method",
            "requires_confirmation",
            "requires_capture",
            "partially_captured",
            "partially_captured_and_capturable",
        ]
    ]

    subscription_id: Optional[str]

    tax: Optional[int]
    """Tax collected in this transaction"""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
