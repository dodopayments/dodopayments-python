# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IntentStatus"]

IntentStatus: TypeAlias = Literal[
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
