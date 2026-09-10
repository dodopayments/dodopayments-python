# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_policies import EmailPolicies
from .email_log_status import EmailLogStatus
from .email_failure_code import EmailFailureCode

__all__ = ["EmailLogItem"]


class EmailLogItem(BaseModel):
    category: str
    """
    The group this email belongs to: payments, refunds, subscriptions,
    dunning_recovery, entitlements or auth.
    """

    created_at: datetime
    """When this email was sent."""

    email_log_id: str
    """Identifies this email. Use it to read the body or to send it again."""

    email_type: str
    """What kind of email this is, for example `payment_successful`."""

    has_preview: bool
    """Whether this email has content to show.

    The content endpoint can still refuse, because the content is removed after 180
    days.
    """

    policies: EmailPolicies
    """What you may do with this email."""

    status: EmailLogStatus
    """Where the email got to: sent, delivered, failed, complained or blocked."""

    failure_code: Optional[EmailFailureCode] = None
    """Why the email did not arrive. It is null unless the email failed."""

    failure_reason: Optional[str] = None
    """A sentence that explains `failure_code`. It is null unless the email failed."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The address the email was sent from."""

    intended_recipient: Optional[str] = None
    """
    What the merchant typed, when test mode redirected the send to the business
    owner.
    """

    recipient: Optional[str] = None
    """The address the email reached."""

    subject: Optional[str] = None
    """The subject line as it was sent. Empty until the provider replicates."""
