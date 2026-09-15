#!/usr/bin/env -S rye run python

import os

from dotenv import load_dotenv

from dodopayments import DodoPayments

load_dotenv()


def main() -> None:
    client = DodoPayments(bearer_token=os.environ["DODO_PAYMENTS_API_KEY"], environment="test_mode")

    session_id = os.environ["DODO_CHECKOUT_SESSION_ID"]

    session = client.checkout_sessions.retrieve(session_id)
    print(f"Session: {session}")


if __name__ == "__main__":
    main()
