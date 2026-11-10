# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .currency import Currency
from .country_code import CountryCode
from .invoice_line import InvoiceLine
from .dunning_state import DunningState
from .intent_status import IntentStatus
from .time_interval import TimeInterval
from .invoice_status import InvoiceStatus
from .collection_method import CollectionMethod

__all__ = [
    "Invoice",
    "Customer",
    "CustomerBillingAddress",
    "Frequency",
    "FrequencyOneTime",
    "FrequencyRecurring",
    "FrequencyMixed",
    "Payment",
    "ReminderSettings",
    "ReminderSettingsSnapshot",
    "ReminderSettingsOverride",
]


class CustomerBillingAddress(BaseModel):
    """A draft can have no country yet. Finalise needs it."""

    city: Optional[str] = None

    country: Optional[CountryCode] = None
    """ISO country code alpha2 variant"""

    state: Optional[str] = None

    street: Optional[str] = None

    zipcode: Optional[str] = None


class Customer(BaseModel):
    billing_address: CustomerBillingAddress
    """A draft can have no country yet. Finalise needs it."""

    cc_emails: List[str]

    customer_id: str

    email: Optional[str] = None

    tax_id: Optional[str] = None


class FrequencyOneTime(BaseModel):
    type: Literal["one_time"]


class FrequencyRecurring(BaseModel):
    count: int

    interval: TimeInterval
    """Unit of a duration count (e.g. license-key validity period)."""

    type: Literal["recurring"]


class FrequencyMixed(BaseModel):
    type: Literal["mixed"]


Frequency: TypeAlias = Annotated[
    Union[FrequencyOneTime, FrequencyRecurring, FrequencyMixed], PropertyInfo(discriminator="type")
]


class Payment(BaseModel):
    amount: int

    created_at: datetime

    payment_id: str

    retry_attempt: Optional[int] = None
    """The automatic charge number. `null` for a payment that the customer started."""

    status: Optional[IntentStatus] = None
    """`null` while the processor has not answered."""


class ReminderSettingsSnapshot(BaseModel):
    """The settings that finalise froze. The reminders run on them."""

    kind: Literal["snapshot"]

    offsets_minutes: List[int]

    paused: bool

    reminders_enabled: bool


class ReminderSettingsOverride(BaseModel):
    """The changes of a draft. A `null` field keeps the business value at finalise."""

    kind: Literal["override"]

    offsets_minutes: Optional[List[int]] = None

    paused: Optional[bool] = None

    reminders_enabled: Optional[bool] = None


ReminderSettings: TypeAlias = Annotated[
    Union[ReminderSettingsSnapshot, ReminderSettingsOverride, None], PropertyInfo(discriminator="kind")
]


class Invoice(BaseModel):
    """An invoice-led invoice.

    Every read and every `invoice.*` webhook uses this schema.
    """

    allowed_actions: List[
        Literal[
            "edit",
            "finalize",
            "delete",
            "send",
            "retry",
            "void",
            "mark_uncollectable",
            "change_dunning",
            "add_note",
            "duplicate",
        ]
    ]
    """The actions that the current status accepts."""

    amount_due: int
    """The amount that the customer must pay.

    Zero unless the invoice is open or past due.
    """

    amount_paid: int
    """The sum of the succeeded payments, in the smallest currency unit.

    A late payment is not included after its late refund.
    """

    amount_refunded: int
    """The sum of the succeeded refunds, in the currency of each payment.

    The late refund of a late payment is not included.
    """

    billing_mode: Literal["normal", "invoice_led"]

    business_id: str

    created_at: datetime

    credits: int
    """Customer credits applied at finalise, in the smallest currency unit.

    Zero or less.
    """

    currency: Currency

    customer: Customer

    discount_ids: List[str]
    """The discount codes of the invoice."""

    editable_fields: List[
        Literal[
            "customer",
            "items",
            "discounts",
            "currency",
            "billing_address",
            "tax_id",
            "review_required",
            "due_at",
            "collection_method",
            "memo",
            "customer_email",
            "cc_emails",
            "dunning",
            "metadata",
        ]
    ]
    """The fields that `PATCH` can change in the current status."""

    frequency: Frequency
    """How often the invoice lines bill.

    `mixed` covers several intervals, or one-time lines next to a plan.
    """

    invoice_id: str

    metadata: object

    refund_ids: List[str]

    retry_count: int
    """The number of failed automatic charges."""

    row_version: int
    """Goes up by one on each change. Use it to ignore an older webhook delivery."""

    status: InvoiceStatus
    """The `message` of each variant is the label of the invoice document."""

    subscription_ids: List[str]

    tags: List[Literal["refunded", "partially_refunded", "disputed", "payment_reversed"]]

    tax: int
    """Tax in the smallest currency unit."""

    total_amount: int
    """Total with tax, before credits, in the smallest currency unit."""

    collection_method: Optional[CollectionMethod] = None

    due_at: Optional[datetime] = None

    dunning_state: Optional[DunningState] = None
    """
    `null` for an invoice that has no collection: draft, paid, void or
    uncollectable.
    """

    finalized_at: Optional[datetime] = None

    hosted_url: Optional[str] = None
    """The page where the customer pays. `null` until the invoice is sent."""

    lines: Optional[List[InvoiceLine]] = None
    """Only on a single invoice. A list leaves it out."""

    memo: Optional[str] = None

    next_reminder_at: Optional[datetime] = None
    """
    The time of the next reminder email to the customer, before or after the due
    date. `null` when no reminder email will go out.
    """

    next_retry_at: Optional[datetime] = None

    payment_terms_days: Optional[int] = None
    """Days from finalise to the due date.

    `null` when the invoice has a custom due date.
    """

    payments: Optional[List[Payment]] = None
    """Only on a single invoice. A list leaves it out."""

    pdf_url: Optional[str] = None

    reminder_settings: Optional[ReminderSettings] = None
    """`null` on a draft that keeps all reminder settings of the business."""

    review_deadline: Optional[datetime] = None
    """The time at which a draft that waits for review finalises."""

    sent_at: Optional[datetime] = None
