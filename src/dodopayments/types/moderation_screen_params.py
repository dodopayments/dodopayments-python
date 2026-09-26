# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ModerationScreenParams"]


class ModerationScreenParams(TypedDict, total=False):
    image: Optional[str]
    """
    The image to screen, as base64, with or without a `data:image/...;base64,`
    prefix. The formats are JPEG, PNG, WebP, GIF and BMP. The limit is 6991530
    base64 characters, and the decoded image must be at most 5 MiB.
    """

    request_id: Optional[str]
    """
    Your identifier for this screen, up to 128 characters, with no control
    characters. The response returns it in `request_id`.
    """

    text: Optional[str]
    """The text to screen, up to 8000 characters."""
