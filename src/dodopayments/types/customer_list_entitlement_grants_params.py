# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CustomerListEntitlementGrantsParams"]


class CustomerListEntitlementGrantsParams(TypedDict, total=False):
    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key", "feature_flag"
    ]
    """Filter by integration type (e.g. `feature_flag`)"""

    page_number: int
    """Page number (default 0)"""

    page_size: int
    """Page size (default 10, max 100)"""

    status: Literal["Pending", "Delivered", "Failed", "Revoked"]
    """Filter by grant status"""
