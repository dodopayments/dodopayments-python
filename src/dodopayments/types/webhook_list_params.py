# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    iterator: Optional[str]
    """The iterator returned from a prior invocation"""

    limit: Optional[int]
    """Limit the number of returned items"""
