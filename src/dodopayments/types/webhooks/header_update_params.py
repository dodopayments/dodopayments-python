# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["HeaderUpdateParams"]


class HeaderUpdateParams(TypedDict, total=False):
    headers: Required[Dict[str, str]]
    """Object of header-value pair to update or add"""
