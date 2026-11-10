# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvoicePreviewExistingParams"]


class InvoicePreviewExistingParams(TypedDict, total=False):
    format: Literal["json", "pdf", "email"]
    """The preview body.

    `json` returns the invoice JSON. `pdf` returns the PDF with a draft mark.
    `email` returns the HTML of the invoice email. A preview saves no row.
    """
