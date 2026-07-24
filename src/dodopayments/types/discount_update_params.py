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

__all__ = ["DiscountUpdateParams", "CurrencyOption"]


class DiscountUpdateParams(TypedDict, total=False):
    amount: Optional[int]
    """
    If present, update the discount amount in **basis points** (e.g., `540` =
    `5.4%`, `10000` = `100%`).

    Must be at least 1 if provided.
    """

    code: Optional[str]
    """If present, update the discount code (uppercase)."""

    currency_options: Optional[Iterable[CurrencyOption]]
    """
    If present, fully replaces the discount's currency options (replace-set
    semantics, like `restricted_to`). Send an empty array to clear them.
    """

    customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]]
    """If present, update who may redeem this discount.

    Plain field (not double-option): the DB column is `NOT NULL`, so it can never be
    cleared back to unset, only changed to another `CustomerEligibility` value.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    metadata: Optional[MetadataParam]
    """Additional metadata for the discount"""

    name: Optional[str]

    per_customer_usage_limit: Optional[int]
    """
    If present, update the per-customer usage limit (double-option: send `null` to
    clear it back to unlimited). Must be `<= usage_limit` (the value in effect after
    this patch) when both are set.
    """

    preserve_on_plan_change: Optional[bool]
    """
    Whether this discount should be preserved when a subscription changes plans. If
    not provided, the existing value is kept.
    """

    restricted_to: Optional[SequenceNotStr[str]]
    """
    If present, replaces all restricted product IDs with this new set. To remove all
    restrictions, send empty array
    """

    starts_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """If present, update `starts_at` (double-option: send `null` to clear it)."""

    subscription_cycles: Optional[int]
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    type: Optional[DiscountType]
    """If present, update the discount type (`percentage` or `flat`)."""

    usage_limit: Optional[int]


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
