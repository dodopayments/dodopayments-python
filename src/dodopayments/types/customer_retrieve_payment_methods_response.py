# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency
from .country_code import CountryCode
from .payment_method_types import PaymentMethodTypes

__all__ = ["CustomerRetrievePaymentMethodsResponse", "Item", "ItemConnectorPaymentMethods", "ItemCard"]


class ItemConnectorPaymentMethods(BaseModel):
    connector_mandate_id: str

    original_payment_authorized_amount: int

    original_payment_authorized_currency: Currency

    payment_method_type: Optional[PaymentMethodTypes] = None


class ItemCard(BaseModel):
    card_issuing_country: Optional[CountryCode] = None
    """ISO country code alpha2 variant"""

    card_network: Optional[str] = None

    card_type: Optional[str] = None

    expiry_month: Optional[str] = None

    expiry_year: Optional[str] = None

    last4_digits: Optional[str] = None


class Item(BaseModel):
    connector_payment_methods: Dict[str, ItemConnectorPaymentMethods]

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
    """PaymentMethod enum from hyperswitch

    https://github.com/juspay/hyperswitch/blob/ecd05d53c99ae701ac94893ec632a3988afe3238/crates/common_enums/src/enums.rs#L2097
    """

    payment_method_id: str

    profile_map: Dict[str, str]

    card: Optional[ItemCard] = None

    last_used_at: Optional[datetime] = None

    recurring_enabled: Optional[bool] = None


class CustomerRetrievePaymentMethodsResponse(BaseModel):
    items: List[Item]
