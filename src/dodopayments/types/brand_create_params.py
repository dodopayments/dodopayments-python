# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    statement_descriptor: Optional[str]

    support_email: Optional[str]

    url: Optional[str]
