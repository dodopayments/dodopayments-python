#!/usr/bin/env -S rye run python
# add fastapi to run this file.

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from dodopayments import DodoPayments

load_dotenv()

app = FastAPI()

client = DodoPayments(
    bearer_token=os.environ["DODO_PAYMENTS_API_KEY"],
    environment="test_mode",
)

class CheckoutRequest(BaseModel):
    product_id: str
    quantity: int = 1

@app.get("/")
def home_root() -> dict[str, str]:
    return {
        "fastAPI checkout status" : "Working!"
    }


@app.post("/checkout")
def create_checkout(request: CheckoutRequest) -> dict[str, Optional[str]]:
    session = client.checkout_sessions.create(
        product_cart=[
            {
                "product_id": request.product_id,
                "quantity": request.quantity,
            }
        ]
    )

    return {
        "session_id": session.session_id,
        "checkout_url": session.checkout_url,
    }