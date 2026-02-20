# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckoutSessionFlagsParam"]


class CheckoutSessionFlagsParam(TypedDict, total=False):
    allow_currency_selection: bool
    """if customer is allowed to change currency, set it to true

    Default is true
    """

    allow_customer_editing_city: bool

    allow_customer_editing_country: bool

    allow_customer_editing_email: bool

    allow_customer_editing_name: bool

    allow_customer_editing_state: bool

    allow_customer_editing_street: bool

    allow_customer_editing_tax_id: bool

    allow_customer_editing_zipcode: bool

    allow_discount_code: bool
    """If the customer is allowed to apply discount code, set it to true.

    Default is true
    """

    allow_phone_number_collection: bool
    """If phone number is collected from customer, set it to rue

    Default is true
    """

    allow_tax_id: bool
    """If the customer is allowed to add tax id, set it to true

    Default is true
    """

    always_create_new_customer: bool
    """
    Set to true if a new customer object should be created. By default email is used
    to find an existing customer to attach the session to

    Default is false
    """

    redirect_immediately: bool
    """If true, redirects the customer immediately after payment completion

    Default is false
    """
