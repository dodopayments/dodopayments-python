# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CustomFieldParam"]


class CustomFieldParam(TypedDict, total=False):
    """Definition of a custom field for checkout"""

    field_type: Required[Literal["text", "number", "email", "url", "date", "dropdown", "boolean"]]
    """Type of field determining validation rules"""

    key: Required[str]
    """Unique identifier for this field (used as key in responses)"""

    label: Required[str]
    """Display label shown to customer"""

    options: Optional[SequenceNotStr[str]]
    """Options for dropdown type (required for dropdown, ignored for others)"""

    placeholder: Optional[str]
    """Placeholder text for the input"""

    required: bool
    """Whether this field is required"""
