# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .theme_config_param import ThemeConfigParam

__all__ = ["CheckoutSessionCustomizationParam"]


class CheckoutSessionCustomizationParam(TypedDict, total=False):
    force_language: Optional[str]
    """Force the checkout interface to render in a specific language (e.g. `en`, `es`)"""

    show_on_demand_tag: bool
    """Show on demand tag

    Default is true
    """

    show_order_details: bool
    """Show order details by default

    Default is true
    """

    theme: Literal["dark", "light", "system"]
    """Theme of the page (determines which mode - light/dark/system - to use)

    Default is `System`.
    """

    theme_config: Optional[ThemeConfigParam]
    """Optional custom theme configuration with colors for light and dark modes"""
