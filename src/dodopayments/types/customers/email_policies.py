# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EmailPolicies"]


class EmailPolicies(BaseModel):
    """What the merchant may do with one row.

    The server decides; the client never
    derives eligibility itself.
    """

    requires_different_address: bool
    """A permanent failure was recorded, so the same address would be a no-op."""

    resend_allowed: bool
    """The row was delivered and may be sent again."""

    resends_remaining: int
    """How many sends are left in this email's chain."""

    retry_allowed: bool
    """The row failed and may be sent again."""
