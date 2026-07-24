# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency
from .metadata import Metadata
from .discount_type import DiscountType

__all__ = ["Discount", "CurrencyOption"]


class CurrencyOption(BaseModel):
    """A per-currency discount option (response shape).

    `max_amount_possible`
    mirrors the DB column of the same name.
    """

    currency: Currency
    """The currency this option applies to."""

    is_default: bool
    """Whether this is the default row FX conversions pivot from."""

    minimum_subtotal: int
    """Eligible-cart threshold in this currency's subunits (0 = no minimum)."""

    max_amount_possible: Optional[int] = None
    """
    The most this code discounts in this currency's subunits (flat deduction or
    percentage cap).
    """


class Discount(BaseModel):
    amount: int
    """The discount amount in **basis points** (e.g., 540 => 5.4%)."""

    business_id: str
    """The business this discount belongs to."""

    code: str
    """The discount code (up to 16 chars)."""

    created_at: datetime
    """Timestamp when the discount is created"""

    customer_eligibility: Literal["any", "first_time", "existing", "specific"]
    """Who may redeem this discount code."""

    discount_id: str
    """The unique discount ID"""

    metadata: Metadata
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """

    preserve_on_plan_change: bool
    """
    Whether this discount should be preserved when a subscription changes plans.
    Default: false (discount is removed on plan change)
    """

    restricted_to: List[str]
    """List of product IDs to which this discount is restricted."""

    times_used: int
    """How many times this discount has been used."""

    type: DiscountType
    """The type of discount (`percentage` or `flat`)."""

    currency_options: Optional[List[CurrencyOption]] = None
    """
    Per-currency options (flat deduction / percentage cap + minimum subtotal). Empty
    for discounts without any configured currency options.
    """

    expires_at: Optional[datetime] = None
    """Optional date/time after which discount is expired."""

    name: Optional[str] = None
    """Name for the Discount"""

    per_customer_usage_limit: Optional[int] = None
    """Maximum number of times a single customer may redeem this discount, if any."""

    starts_at: Optional[datetime] = None
    """Optional date/time before which the discount is not yet active.

    NULL = active immediately.
    """

    subscription_cycles: Optional[int] = None
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    usage_limit: Optional[int] = None
    """Usage limit for this discount, if any."""
