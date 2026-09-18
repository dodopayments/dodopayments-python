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

    payment_id = os.environ["DODO_PAYMENT_ID"]

    refund = client.refunds.create(
        payment_id=payment_id,
    )

    print("Refund created")
    print(refund)


if __name__ == "__main__":
    main()
