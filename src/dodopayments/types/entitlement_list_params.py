# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EntitlementListParams"]


class EntitlementListParams(TypedDict, total=False):
    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
    ]
    """Filter by integration type"""

    page_number: int
    """Page number (default 0)"""

    page_size: int
    """Page size (default 10, max 100)"""
