# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AttachProductEntitlementParam"]


class AttachProductEntitlementParam(TypedDict, total=False):
    """Request struct for attaching an entitlement to a product.

    Mirrors the `credit_entitlements` attach shape — every "attach something
    to a product" array takes objects, not bare IDs. Uniform shape leaves
    room for per-attachment settings later without another API break.
    """

    entitlement_id: Required[str]
    """ID of the entitlement to attach to the product"""
