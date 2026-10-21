# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .add_meter_to_price import AddMeterToPrice

__all__ = ["Price", "OneTimePrice", "RecurringPrice", "UsageBasedPrice"]


class OneTimePrice(BaseModel):
    """One-time price details."""

    currency: Currency
    """The currency in which the payment is made."""

    price: int
    """
    The payment amount, in the smallest denomination of the currency (e.g., cents
    for USD). For example, to charge $1.00, pass `100`.

    If [`pay_what_you_want`](Self::pay_what_you_want) is set to `true`, this field
    represents the **minimum** amount the customer must pay.
    """

    type: Literal["one_time_price"]

    discount: Optional[int] = None
    """Deprecated: use `discount_bps` instead.

    Discount applied to the price, represented as a percentage (0 to 100). A
    response rounds this value to the nearest whole percent. Defaults to `0`.
    """

    discount_bps: Optional[int] = None
    """Discount applied to the price, in basis points.

    100 basis points make one percent, so `1250` is a discount of 12.5%.

    Use this field for a discount with a fraction of a percent. A request that sends
    this field ignores `discount`. A value of `0` gives no discount.
    """

    pay_what_you_want: Optional[bool] = None
    """
    Indicates whether the customer can pay any amount they choose. If set to `true`,
    the [`price`](Self::price) field is the minimum amount.
    """

    purchasing_power_parity: Optional[bool] = None
    """Opts this price in to purchasing power parity.

    The business must also enable purchasing power parity. The discount percentage
    per country is always business-wide. Defaults to `false`.
    """

    suggested_price: Optional[int] = None
    """A suggested price for the user to pay.

    This value is only considered if [`pay_what_you_want`](Self::pay_what_you_want)
    is `true`. Otherwise, it is ignored.
    """

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive."""


class RecurringPrice(BaseModel):
    """Recurring price details."""

    currency: Currency
    """The currency in which the payment is made."""

    payment_frequency_count: int
    """
    Number of `payment_frequency_interval` units between two charges. This field
    sets the billing cycle. For example, `1` with a `payment_frequency_interval` of
    `month` charges the customer every month.
    """

    payment_frequency_interval: TimeInterval
    """
    The time unit of the billing cycle (e.g., day, month, year). Use it with
    `payment_frequency_count`.
    """

    price: int
    """The payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    subscription_period_count: int
    """
    Number of `subscription_period_interval` units for the total duration of the
    subscription. This field does not set the billing cycle. Use
    `payment_frequency_count` for the billing cycle. When this period ends, the
    subscription expires. Dodo Payments does not start a new billing cycle after the
    subscription expires. Dodo Payments can still retry a failed payment for an
    earlier billing cycle.

    For a subscription that renews until the customer cancels it, set this to `20`
    with a `subscription_period_interval` of `year`. This is the recommended value
    and also the maximum. The subscription expires after 20 years if the customer
    does not cancel it before then.

    For example, a monthly plan uses a `payment_frequency_count` of `1`, a
    `payment_frequency_interval` of `month`, and a subscription period of `20`
    `year`. Do not set the subscription period to `1` `month` for a monthly plan:
    the subscription then expires after one month.
    """

    subscription_period_interval: TimeInterval
    """
    The time unit of the total subscription duration (e.g., day, month, year). Use
    it with `subscription_period_count`. The recommended value is `year`, with a
    `subscription_period_count` of `20`.
    """

    type: Literal["recurring_price"]

    discount: Optional[int] = None
    """Deprecated: use `discount_bps` instead.

    Discount applied to the price, represented as a percentage (0 to 100). A
    response rounds this value to the nearest whole percent. Defaults to `0`.
    """

    discount_bps: Optional[int] = None
    """Discount applied to the price, in basis points.

    100 basis points make one percent, so `1250` is a discount of 12.5%.

    Use this field for a discount with a fraction of a percent. A request that sends
    this field ignores `discount`. A value of `0` gives no discount.
    """

    purchasing_power_parity: Optional[bool] = None
    """Opts this price in to purchasing power parity.

    The business must also enable purchasing power parity. The discount percentage
    per country is always business-wide. Defaults to `false`.
    """

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive"""

    trial_amount: Optional[int] = None
    """
    Amount charged today for a paid trial, in the price currency's minor units.
    Requires `trial_period_days > 0`. Omit or null for a free trial (the default).
    """

    trial_apply_discounts: Optional[bool] = None
    """Whether discount codes reduce the trial charge.

    Defaults to false. Only meaningful when a paid trial is configured.
    """

    trial_payment_method_optional: Optional[bool] = None
    """Let a customer start a free trial with no card. Defaults to false."""

    trial_period_days: Optional[int] = None
    """Number of days for the trial period. A value of `0` indicates no trial period."""

    zero_amount_payment_method_optional: Optional[bool] = None
    """
    Let a customer start a subscription with no card, when the amount due today is
    `0` (a native `0` price, or a 100% discount). Defaults to false.
    """


class UsageBasedPrice(BaseModel):
    """Usage Based price details."""

    currency: Currency
    """The currency in which the payment is made."""

    fixed_price: int
    """The fixed payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    payment_frequency_count: int
    """
    Number of `payment_frequency_interval` units between two charges. This field
    sets the billing cycle. For example, `1` with a `payment_frequency_interval` of
    `month` charges the customer every month.
    """

    payment_frequency_interval: TimeInterval
    """
    The time unit of the billing cycle (e.g., day, month, year). Use it with
    `payment_frequency_count`.
    """

    subscription_period_count: int
    """
    Number of `subscription_period_interval` units for the total duration of the
    subscription. This field does not set the billing cycle. Use
    `payment_frequency_count` for the billing cycle. When this period ends, the
    subscription expires. Dodo Payments does not start a new billing cycle after the
    subscription expires. Dodo Payments can still retry a failed payment for an
    earlier billing cycle.

    For a subscription that renews until the customer cancels it, set this to `20`
    with a `subscription_period_interval` of `year`. This is the recommended value
    and also the maximum. The subscription expires after 20 years if the customer
    does not cancel it before then.

    For example, a monthly plan uses a `payment_frequency_count` of `1`, a
    `payment_frequency_interval` of `month`, and a subscription period of `20`
    `year`. Do not set the subscription period to `1` `month` for a monthly plan:
    the subscription then expires after one month.
    """

    subscription_period_interval: TimeInterval
    """
    The time unit of the total subscription duration (e.g., day, month, year). Use
    it with `subscription_period_count`. The recommended value is `year`, with a
    `subscription_period_count` of `20`.
    """

    type: Literal["usage_based_price"]

    discount: Optional[int] = None
    """Deprecated: use `discount_bps` instead.

    Discount applied to the price, represented as a percentage (0 to 100). A
    response rounds this value to the nearest whole percent. Defaults to `0`.
    """

    discount_bps: Optional[int] = None
    """Discount applied to the price, in basis points.

    100 basis points make one percent, so `1250` is a discount of 12.5%.

    Use this field for a discount with a fraction of a percent. A request that sends
    this field ignores `discount`. A value of `0` gives no discount.
    """

    meters: Optional[List[AddMeterToPrice]] = None

    purchasing_power_parity: Optional[bool] = None
    """Opts this price in to purchasing power parity.

    The business must also enable purchasing power parity. The discount percentage
    per country is always business-wide. Applies to the fixed fee only, never to
    metered usage. Defaults to `false`.
    """

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive"""


Price: TypeAlias = Annotated[Union[OneTimePrice, RecurringPrice, UsageBasedPrice], PropertyInfo(discriminator="type")]
