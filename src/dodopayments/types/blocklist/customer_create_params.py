# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .blocked_customer_source import BlockedCustomerSource

__all__ = ["CustomerCreateParams", "BlocklistCustomersBlockByCustomerID", "BlocklistCustomersBlockByEmail"]


class BlocklistCustomersBlockByCustomerID(TypedDict, total=False):
    customer_id: Required[str]
    """Customer to block. The block still applies to that customer's email."""

    reason: Optional[str]
    """Why the merchant blocked this customer. The entry page shows it."""

    source: Optional[BlockedCustomerSource]
    """Screen the merchant blocked from.

    Ignored for an API-key caller, whose entry always records `api`. A dashboard
    caller that omits it records `blocklist_page`.
    """


class BlocklistCustomersBlockByEmail(TypedDict, total=False):
    email: Required[str]
    """Email to block. It must belong to an existing customer of this business."""

    reason: Optional[str]
    """Why the merchant blocked this customer. The entry page shows it."""

    source: Optional[BlockedCustomerSource]
    """Screen the merchant blocked from.

    Ignored for an API-key caller, whose entry always records `api`. A dashboard
    caller that omits it records `blocklist_page`.
    """


CustomerCreateParams: TypeAlias = Union[BlocklistCustomersBlockByCustomerID, BlocklistCustomersBlockByEmail]
