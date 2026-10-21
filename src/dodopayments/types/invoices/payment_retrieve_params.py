# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentRetrieveParams"]


class PaymentRetrieveParams(TypedDict, total=False):
    token: str
    """The signed link token.

    If the business asks for a credential on its invoice links, a valid token for
    this record replaces the credential.
    """
