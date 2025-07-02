# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerPortalCreateParams"]


class CustomerPortalCreateParams(TypedDict, total=False):
    send_email: bool
    """If true, will send link to user."""
