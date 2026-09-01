# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockByCustomerIDParam"]


class BlockByCustomerIDParam(TypedDict, total=False):
    customer_id: Required[str]
    """Customer to block. The block still applies to that customer's email."""
