# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .country_code import CountryCode
from .payment_method_types import PaymentMethodTypes

__all__ = ["CustomerRetrievePaymentMethodsResponse", "Item", "ItemCard"]


class ItemCard(BaseModel):
    card_holder_name: Optional[str] = None

    card_issuing_country: Optional[CountryCode] = None
    """ISO country code alpha2 variant"""

    card_network: Optional[str] = None

    card_type: Optional[str] = None

    expiry_month: Optional[str] = None

    expiry_year: Optional[str] = None

    last4_digits: Optional[str] = None


class Item(BaseModel):
    payment_method: Literal[
        "card",
        "card_redirect",
        "pay_later",
        "wallet",
        "bank_redirect",
        "bank_transfer",
        "crypto",
        "bank_debit",
        "reward",
        "real_time_payment",
        "upi",
        "voucher",
        "gift_card",
        "open_banking",
        "mobile_payment",
    ]

    payment_method_id: str

    card: Optional[ItemCard] = None

    last_used_at: Optional[datetime] = None

    payment_method_type: Optional[PaymentMethodTypes] = None

    recurring_enabled: Optional[bool] = None


class CustomerRetrievePaymentMethodsResponse(BaseModel):
    items: List[Item]
