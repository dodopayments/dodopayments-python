# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentMethodTypes"]

PaymentMethodTypes: TypeAlias = Literal[
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
    "paypal",
    "affirm",
    "klarna",
    "sepa",
    "ach",
    "amazon_pay",
    "afterpay_clearpay",
]
