# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentRetrievePayoutParams"]


class PaymentRetrievePayoutParams(TypedDict, total=False):
    token: str
    """The signed link token. A valid token for this record replaces the credential."""
