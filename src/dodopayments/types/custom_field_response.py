# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomFieldResponse"]


class CustomFieldResponse(BaseModel):
    """Customer's response to a custom field"""

    key: str
    """Key matching the custom field definition"""

    value: str
    """Value provided by customer"""
