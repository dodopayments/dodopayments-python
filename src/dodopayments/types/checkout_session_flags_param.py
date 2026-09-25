# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckoutSessionFlagsParam"]


class CheckoutSessionFlagsParam(TypedDict, total=False):
    allow_currency_selection: bool
    """if customer is allowed to change currency, set it to true

    Default is true
    """

    allow_customer_editing_business_name: bool
    """
    If true, the customer can supply or edit the business name associated with the
    tax id during checkout. Works independently of `allow_customer_editing_tax_id` —
    either flag (or `allow_tax_id`) is sufficient to let the customer override the
    session's business name. Typically set together with
    `allow_customer_editing_tax_id`.

    Default is false
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

    allow_editing_addons: bool
    """
    If true, the customer can add or remove addons on a subscription product during
    checkout.

    Default is false
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

    require_cardholder_name: bool
    """
    If true, the customer must give the name on the card to pay by card. The
    checkout page enforces this. Other payment methods ignore it.

    Default is false
    """

    require_phone_number: bool
    """
    If true, the customer must provide a phone number to complete checkout. Requires
    `allow_phone_number_collection` to also be true.

    Default is false
    """

    require_tax_id: bool
    """
    If true, the customer must give a tax id to check out as a business. A tax id is
    the GST number in India, or the VAT number in the EU. You must also set
    `allow_tax_id` to true.

    On the checkout page, this field does not change checkout for a customer who
    buys as an individual.

    A `confirm: true` request skips the checkout page. The request must contain
    `tax_id`.

    Default is false
    """

    single_page: bool
    """
    If true, the session uses the single-page checkout flow: the page initializes
    the payment at load time and confirms it in place, with no separate payment
    page.

    Default is false
    """
