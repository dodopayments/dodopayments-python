#!/usr/bin/env -S rye run python

import os

from dotenv import load_dotenv

from dodopayments import DodoPayments

load_dotenv()

def main() -> None:
    client = DodoPayments(
        bearer_token=os.environ["DODO_PAYMENTS_API_KEY"],
        environment="test_mode",
    )

    checkout_session = client.checkout_sessions.create(
        product_cart=[
            {
                "product_id": os.environ["DODO_PRODUCT_ID"],
                "quantity": 1,
            }
        ],
    )

    print(f"Checkout Session ID: {checkout_session.session_id}")


if __name__ == "__main__":
    main()