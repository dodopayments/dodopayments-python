# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceLine"]


class InvoiceLine(BaseModel):
    """One frozen line. Amounts are in the smallest currency unit."""

    amount: int

    kind: Literal["subscription", "addon", "meter", "credit_overage", "one_time"]

    quantity: int
    """A usage line has a quantity of 1. Its amount is the full usage charge."""

    tax: int

    tax_inclusive: bool
    """`true` when `amount` includes `tax`."""

    unit_amount: int

    addon_id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    period_end: Optional[datetime] = None

    period_start: Optional[datetime] = None

    product_id: Optional[str] = None

    subscription_id: Optional[str] = None

    tax_rate: Optional[int] = None
    """Tax percent times 100. For example, 1800 is 18%."""
