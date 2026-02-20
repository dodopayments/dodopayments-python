# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .theme_mode_config_param import ThemeModeConfigParam

__all__ = ["ThemeConfigParam"]


class ThemeConfigParam(TypedDict, total=False):
    """Custom theme configuration with colors for light and dark modes."""

    dark: Optional[ThemeModeConfigParam]
    """Dark mode color configuration"""

    font_primary_url: Optional[str]
    """URL for the primary font. Must be a valid https:// URL."""

    font_secondary_url: Optional[str]
    """URL for the secondary font. Must be a valid https:// URL."""

    font_size: Optional[Literal["xs", "sm", "md", "lg", "xl", "2xl"]]
    """Font size for the checkout UI"""

    font_weight: Optional[Literal["normal", "medium", "bold", "extraBold"]]
    """Font weight for the checkout UI"""

    light: Optional[ThemeModeConfigParam]
    """Light mode color configuration"""

    pay_button_text: Optional[str]
    """Custom text for the pay button (e.g., "Complete Purchase", "Subscribe Now").

    Max 100 characters.
    """

    radius: Optional[str]
    """Border radius for UI elements.

    Must be a number followed by px, rem, or em (e.g., "4px", "0.5rem", "1em")
    """
