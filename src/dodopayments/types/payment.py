# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .refund import Refund
from .dispute import Dispute
from .._models import BaseModel

__all__ = ["Payment", "Customer", "ProductCart"]


class Customer(BaseModel):
    customer_id: str

    email: str

    name: str


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class Payment(BaseModel):
    business_id: str

    created_at: datetime

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

    customer: Customer

    disputes: List[Dispute]

    metadata: Dict[str, str]

    payment_id: str

    refunds: List[Refund]

    total_amount: int
    """Total amount taken from the customer including tax"""

    payment_link: Optional[str] = None

    payment_method: Optional[str] = None

    payment_method_type: Optional[str] = None

    product_cart: Optional[List[ProductCart]] = None
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
    ] = None

    subscription_id: Optional[str] = None

    tax: Optional[int] = None
    """Tax collected in this transaction"""

    updated_at: Optional[datetime] = None
