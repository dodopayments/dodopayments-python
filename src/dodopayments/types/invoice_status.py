# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["InvoiceStatus"]

InvoiceStatus: TypeAlias = Literal["open", "paid", "void", "draft", "past_due", "uncollectable"]
