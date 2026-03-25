# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomFieldResponseParam"]


class CustomFieldResponseParam(TypedDict, total=False):
    """Customer's response to a custom field"""

    key: Required[str]
    """Key matching the custom field definition"""

    value: Required[str]
    """Value provided by customer"""
