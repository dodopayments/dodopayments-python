# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .currency import Currency
from .discount_type import DiscountType
from .metadata_param import MetadataParam

__all__ = ["DiscountCreateParams", "CurrencyOption"]


class DiscountCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The discount amount in **basis points** (e.g.

    `540` means `5.4%`, `10000` means `100%`).

    Must be at least 1.
    """

    type: Required[DiscountType]
    """The discount type: `percentage` or `flat` (`flat_per_unit` stays blocked)."""

    code: Optional[str]
    """Optionally supply a code (will be uppercased).

    - Must be at least 3 characters if provided.
    - If omitted, a random 16-character code is generated.
    """

    currency_options: Optional[Iterable[CurrencyOption]]
    """
    Per-currency options (flat deduction / percentage cap + minimum subtotal).
    Required for `flat` codes (must include a resolvable default); optional
    per-currency caps for `percentage` codes. Per-row invariants are checked in
    `normalize_currency_options`, not via `#[validate(nested)]`.
    """

    customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]]
    """Who may redeem this discount code.

    Defaults to `any` (unrestricted). `specific` starts with zero attached customers
    (fails closed) until customers are attached via
    `POST /discounts/{id}/customers`.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the discount expires, if ever."""

    metadata: MetadataParam
    """Additional metadata for the discount"""

    name: Optional[str]

    per_customer_usage_limit: Optional[int]
    """
    Maximum number of times a single customer may redeem this discount. Must be
    `<= usage_limit` when both are set.
    """

    preserve_on_plan_change: bool
    """
    Whether this discount should be preserved when a subscription changes plans.
    Default: false (discount is removed on plan change)
    """

    restricted_to: Optional[SequenceNotStr[str]]
    """List of product IDs to restrict usage (if any)."""

    starts_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    When the discount becomes active, if scheduled for the future. NULL = active
    immediately. Must be strictly before `expires_at` when both are set.
    """

    subscription_cycles: Optional[int]
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    usage_limit: Optional[int]
    """How many times this discount can be used (if any). Must be >= 1 if provided."""


class CurrencyOption(TypedDict, total=False):
    """A per-currency discount option (request shape).

    `max_amount_possible` is the most this code discounts in this currency — the
    flat deduction for `flat` codes, or the max-discount cap for `percentage`
    codes. Maps to the DB column of the same name.
    """

    currency: Required[Currency]
    """The currency this option applies to."""

    is_default: bool
    """Whether this row is the default to convert from for unconfigured currencies.

    At most one row per discount may be default.
    """

    max_amount_possible: Optional[int]
    """The most this code discounts in this currency's subunits.

    For `flat` codes this is the deduction; for `percentage` codes it is the
    max-discount cap. Must be > 0 if provided.
    """

    minimum_subtotal: int
    """Eligible-cart threshold in this currency's subunits (0 = no minimum)."""
