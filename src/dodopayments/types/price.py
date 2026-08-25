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

    discount: int
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    price: int
    """
    The payment amount, in the smallest denomination of the currency (e.g., cents
    for USD). For example, to charge $1.00, pass `100`.

    If [`pay_what_you_want`](Self::pay_what_you_want) is set to `true`, this field
    represents the **minimum** amount the customer must pay.
    """

    type: Literal["one_time_price"]

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

    discount: int
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    payment_frequency_count: int
    """
    Number of units for the payment frequency. For example, a value of `1` with a
    `payment_frequency_interval` of `month` represents monthly payments.
    """

    payment_frequency_interval: TimeInterval
    """The time interval for the payment frequency (e.g., day, month, year)."""

    price: int
    """The payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    subscription_period_count: int
    """
    Number of units for the subscription period. For example, a value of `12` with a
    `subscription_period_interval` of `month` represents a one-year subscription.
    """

    subscription_period_interval: TimeInterval
    """The time interval for the subscription period (e.g., day, month, year)."""

    type: Literal["recurring_price"]

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

    trial_period_days: Optional[int] = None
    """Number of days for the trial period. A value of `0` indicates no trial period."""


class UsageBasedPrice(BaseModel):
    """Usage Based price details."""

    currency: Currency
    """The currency in which the payment is made."""

    discount: int
    """Discount applied to the price, represented as a percentage (0 to 100)."""

    fixed_price: int
    """The fixed payment amount.

    Represented in the lowest denomination of the currency (e.g., cents for USD).
    For example, to charge $1.00, pass `100`.
    """

    payment_frequency_count: int
    """
    Number of units for the payment frequency. For example, a value of `1` with a
    `payment_frequency_interval` of `month` represents monthly payments.
    """

    payment_frequency_interval: TimeInterval
    """The time interval for the payment frequency (e.g., day, month, year)."""

    subscription_period_count: int
    """
    Number of units for the subscription period. For example, a value of `12` with a
    `subscription_period_interval` of `month` represents a one-year subscription.
    """

    subscription_period_interval: TimeInterval
    """The time interval for the subscription period (e.g., day, month, year)."""

    type: Literal["usage_based_price"]

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
