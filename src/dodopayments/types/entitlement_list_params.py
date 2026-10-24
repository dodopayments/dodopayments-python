# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EntitlementListParams"]


class EntitlementListParams(TypedDict, total=False):
    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key", "feature_flag"
    ]
    """Filter by integration type"""

    locale: str
    """
    Shows the translated name, description and unit of the catalog entities in this
    locale. The value must be a code from `GET /locales`, for example `fr`. A field
    with no translation, an unknown code, or no code shows the base text.

    Do not send a text from a localized response back in a create or update request.
    The base text then changes to the translated text.
    """

    page_number: int
    """Page number (default 0)"""

    page_size: int
    """Page size (default 10, max 100)"""
