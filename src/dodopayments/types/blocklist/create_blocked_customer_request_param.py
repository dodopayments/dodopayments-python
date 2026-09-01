# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias

from .block_by_email_param import BlockByEmailParam
from .blocked_customer_source import BlockedCustomerSource
from .block_by_customer_id_param import BlockByCustomerIDParam

__all__ = ["CreateBlockedCustomerRequestParam", "BlocklistCustomersBlockByCustomerID", "BlocklistCustomersBlockByEmail"]


class BlocklistCustomersBlockByCustomerID(BlockByCustomerIDParam, total=False):
    reason: Optional[str]
    """Why the merchant blocked this customer. The entry page shows it."""

    source: Optional[BlockedCustomerSource]
    """Screen the merchant blocked from.

    Ignored for an API-key caller, whose entry always records `api`. A dashboard
    caller that omits it records `blocklist_page`.
    """


class BlocklistCustomersBlockByEmail(BlockByEmailParam, total=False):
    reason: Optional[str]
    """Why the merchant blocked this customer. The entry page shows it."""

    source: Optional[BlockedCustomerSource]
    """Screen the merchant blocked from.

    Ignored for an API-key caller, whose entry always records `api`. A dashboard
    caller that omits it records `blocklist_page`.
    """


CreateBlockedCustomerRequestParam: TypeAlias = Union[
    BlocklistCustomersBlockByCustomerID, BlocklistCustomersBlockByEmail
]
