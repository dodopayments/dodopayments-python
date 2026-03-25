# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerPortalCreateParams"]


class CustomerPortalCreateParams(TypedDict, total=False):
    return_url: str
    """Optional return URL for this session.

    Overrides the business-level default. This URL will be shown as a "Return to
    {business}" back button in the portal.
    """

    send_email: bool
    """If true, will send link to user."""
