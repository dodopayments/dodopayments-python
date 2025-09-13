# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .customer_wallet import CustomerWallet

__all__ = ["WalletListResponse"]


class WalletListResponse(BaseModel):
    items: List[CustomerWallet]

    total_balance_usd: int
    """Sum of all wallet balances converted to USD (in smallest unit)"""
