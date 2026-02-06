# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ThemeModeConfigParam"]


class ThemeModeConfigParam(TypedDict, total=False):
    """Color configuration for a single theme mode (light or dark).

    All color fields accept standard CSS color formats:
    - Hex: `#fff`, `#ffffff`, `#ffffffff` (with or without # prefix)
    - RGB/RGBA: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`
    - HSL/HSLA: `hsl(120, 100%, 50%)`, `hsla(120, 100%, 50%, 0.5)`
    - Named colors: `red`, `blue`, `transparent`, etc.
    - Advanced: `hwb()`, `lab()`, `lch()`, `oklab()`, `oklch()`, `color()`
    """

    bg_primary: Optional[str]
    """Background primary color

    Examples: `"#ffffff"`, `"rgb(255, 255, 255)"`, `"white"`
    """

    bg_secondary: Optional[str]
    """Background secondary color"""

    border_primary: Optional[str]
    """Border primary color"""

    border_secondary: Optional[str]
    """Border secondary color"""

    button_primary: Optional[str]
    """Primary button background color"""

    button_primary_hover: Optional[str]
    """Primary button hover color"""

    button_secondary: Optional[str]
    """Secondary button background color"""

    button_secondary_hover: Optional[str]
    """Secondary button hover color"""

    button_text_primary: Optional[str]
    """Primary button text color"""

    button_text_secondary: Optional[str]
    """Secondary button text color"""

    input_focus_border: Optional[str]
    """Input focus border color"""

    text_error: Optional[str]
    """Text error color"""

    text_placeholder: Optional[str]
    """Text placeholder color"""

    text_primary: Optional[str]
    """Text primary color"""

    text_secondary: Optional[str]
    """Text secondary color"""

    text_success: Optional[str]
    """Text success color"""
