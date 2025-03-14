# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .refund import Refund
from .dispute import Dispute
from .._models import BaseModel
from .intent_status import IntentStatus
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["Payment", "ProductCart"]


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class Payment(BaseModel):
    business_id: str
    """Identifier of the business associated with the payment"""

    created_at: datetime
    """Timestamp when the payment was created"""

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

    customer: CustomerLimitedDetails

    disputes: List[Dispute]
    """List of disputes associated with this payment"""

    metadata: Dict[str, str]

    payment_id: str
    """Unique identifier for the payment"""

    refunds: List[Refund]
    """List of refunds issued for this payment"""

    total_amount: int
    """
    Total amount charged to the customer including tax, in smallest currency unit
    (e.g. cents)
    """

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    error_message: Optional[str] = None
    """An error message if the payment failed"""

    payment_link: Optional[str] = None
    """Checkout URL"""

    payment_method: Optional[str] = None
    """Payment method used by customer (e.g. "card", "bank_transfer")"""

    payment_method_type: Optional[str] = None
    """Specific type of payment method (e.g. "visa", "mastercard")"""

    product_cart: Optional[List[ProductCart]] = None
    """List of products purchased in a one-time payment"""

    status: Optional[IntentStatus] = None

    subscription_id: Optional[str] = None
    """Identifier of the subscription if payment is part of a subscription"""

    tax: Optional[int] = None
    """Amount of tax collected in smallest currency unit (e.g. cents)"""

    updated_at: Optional[datetime] = None
    """Timestamp when the payment was last updated"""
