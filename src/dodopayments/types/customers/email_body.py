# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .email_failure_code import EmailFailureCode

__all__ = ["EmailBody"]


class EmailBody(BaseModel):
    merchant_authored: bool
    """Whether the merchant wrote this content.

    It is true for the recovery and dunning emails, which the merchant writes.

    The content is email HTML. Render it in a sandbox, whatever this value is.
    """

    failure_code: Optional[EmailFailureCode] = None
    """Why the email did not arrive. It is null unless the email failed."""

    failure_reason: Optional[str] = None
    """A sentence that explains `failure_code`. It is null unless the email failed."""

    html: Optional[str] = None
    """The stored HTML. It is null on a text-only email."""

    text: Optional[str] = None
    """The stored plain text."""
