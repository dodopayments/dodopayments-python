#!/usr/bin/env -S rye run python

import os

from dotenv import load_dotenv

from dodopayments import DodoPayments

load_dotenv()

def main() -> None:
    client = DodoPayments(
        bearer_token=os.environ["DODO_PAYMENTS_API_KEY"],
        environment="test_mode"
    )

    subscription_id = os.environ["DODO_SUBSCRIPTION_ID"]
    subscription = client.subscriptions.retrieve(subscription_id)

    print("Current subscription:")
    print(subscription)

    client.subscriptions.update(
        subscription_id,
        cancel_at_next_billing_date= True
    )

    print("Subscription cancelled")

if __name__ == "__main__":
    main()