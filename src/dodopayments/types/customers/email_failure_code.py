# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EmailFailureCode"]

EmailFailureCode: TypeAlias = Literal[
    "mailbox_not_found",
    "address_rejected",
    "address_suppressed",
    "mailbox_full",
    "temporary_failure",
    "message_too_large",
    "marked_as_spam",
    "send_failed",
]
