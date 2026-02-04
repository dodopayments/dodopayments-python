"""
FastAPI integration for DodoPayments webhooks.

This module provides a dependency for FastAPI applications to verify DodoPayments webhook signatures.
"""

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated

try:
    from fastapi import Depends, Header, HTTPException, Request, status
    from fastapi.datastructures import Headers
except ImportError:
    raise ImportError(
        "You need to install `fastapi` to use this module. "
        "Install it with `pip install fastapi` or `pip install dodopayments[fastapi]`."
    )

try:
    from standardwebhooks import Webhook
    from standardwebhooks.webhooks import WebhookVerificationError
except ImportError:
    raise ImportError(
        "You need to install `standardwebhooks` to use this module. "
        "Install it with `pip install standardwebhooks` or `pip install dodopayments[webhooks]`."
    )

from .._client import DodoPayments
from ..types.unwrap_webhook_event import UnwrapWebhookEvent


class DodoWebhookGuard:
    """
    FastAPI dependency for verifying DodoPayments webhook signatures.
    
    This class provides a dependency that can be used with FastAPI's Depends() to
    verify webhook signatures and extract the payload data.
    
    Example:
        from fastapi import FastAPI, Depends
        from dodopayments.integrations.fastapi import DodoWebhookGuard
        
        app = FastAPI()
        guard = DodoWebhookGuard(webhook_key="your_webhook_key")
        
        @app.post("/webhook")
        async def handle_webhook(data: UnwrapWebhookEvent = Depends(guard.verify)):
            # Process the verified webhook data
            print(f"Received webhook event: {data.event_type}")
            return {"status": "ok"}
    """
    
    def __init__(self, webhook_key: Optional[Union[str, bytes]] = None, client: Optional[DodoPayments] = None):
        """
        Initialize the DodoWebhookGuard.
        
        Args:
            webhook_key: The webhook signing secret. If not provided, it will be taken from the client.
            client: The DodoPayments client instance. Used to get the webhook key if not provided directly.
        """
        self._webhook_key = webhook_key
        self._client = client
    
    def _get_webhook_key(self) -> Union[str, bytes]:
        """Get the webhook key from the provided key or client."""
        if self._webhook_key is not None:
            return self._webhook_key
            
        if self._client is not None and self._client.webhook_key is not None:
            return self._client.webhook_key
            
        raise ValueError(
            "Cannot verify a webhook without a key. "
            "Provide a webhook_key parameter or use a client with webhook_key configured."
        )
    
    async def verify(
        self,
        request: Request,
        webhook_id: Annotated[str, Header(alias="webhook-id")],
        webhook_timestamp: Annotated[str, Header(alias="webhook-timestamp")],
        webhook_signature: Annotated[str, Header(alias="webhook-signature")],
    ) -> UnwrapWebhookEvent:
        """
        Verify the webhook signature and extract the payload data.
        
        This method is designed to be used as a FastAPI dependency.
        
        Args:
            request: The FastAPI Request object.
            webhook_id: The webhook ID from the header.
            webhook_timestamp: The webhook timestamp from the header.
            webhook_signature: The webhook signature from the header.
            
        Returns:
            The parsed webhook event data.
            
        Raises:
            HTTPException: If the webhook signature verification fails.
        """
        # Extract the payload
        payload = (await request.body()).decode("utf-8")
        
        # Prepare headers for verification
        headers = {
            "webhook-id": webhook_id,
            "webhook-timestamp": webhook_timestamp,
            "webhook-signature": webhook_signature,
        }
        
        # Get the webhook key
        key = self._get_webhook_key()
        
        # Verify the webhook
        try:
            Webhook(key).verify(payload, headers)
        except WebhookVerificationError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Webhook signature verification failed",
            ) from e
        
        # Parse and return the webhook event
        try:
            from ..resources.webhooks.webhooks import WebhooksResource
            return WebhooksResource(self._client or DodoPayments()).unwrap(payload, headers=headers, key=key)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to parse webhook payload",
            ) from e


# Convenience function for simpler usage
def get_dodo_webhook_guard(
    webhook_key: Optional[Union[str, bytes]] = None,
    client: Optional[DodoPayments] = None,
) -> DodoWebhookGuard:
    """
    Create a DodoWebhookGuard instance.
    
    Args:
        webhook_key: The webhook signing secret.
        client: The DodoPayments client instance.
        
    Returns:
        A DodoWebhookGuard instance.
    """
    return DodoWebhookGuard(webhook_key=webhook_key, client=client)