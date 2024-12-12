# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, DodoPaymentsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "DodoPayments",
    "AsyncDodoPayments",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://test.dodopayments.com/",
    "environment_1": "https://live.dodopayments.com/",
}


class DodoPayments(SyncAPIClient):
    checkout: resources.CheckoutResource
    customers: resources.CustomersResource
    disputes: resources.DisputesResource
    payments: resources.PaymentsResource
    payouts: resources.PayoutsResource
    products: resources.ProductsResource
    refunds: resources.RefundsResource
    subscriptions: resources.SubscriptionsResource
    webhook_events: resources.WebhookEventsResource
    outgoing_webhooks: resources.OutgoingWebhooksResource
    with_raw_response: DodoPaymentsWithRawResponse
    with_streaming_response: DodoPaymentsWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous dodo-payments client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise DodoPaymentsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("DODO_PAYMENTS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `DODO_PAYMENTS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.checkout = resources.CheckoutResource(self)
        self.customers = resources.CustomersResource(self)
        self.disputes = resources.DisputesResource(self)
        self.payments = resources.PaymentsResource(self)
        self.payouts = resources.PayoutsResource(self)
        self.products = resources.ProductsResource(self)
        self.refunds = resources.RefundsResource(self)
        self.subscriptions = resources.SubscriptionsResource(self)
        self.webhook_events = resources.WebhookEventsResource(self)
        self.outgoing_webhooks = resources.OutgoingWebhooksResource(self)
        self.with_raw_response = DodoPaymentsWithRawResponse(self)
        self.with_streaming_response = DodoPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDodoPayments(AsyncAPIClient):
    checkout: resources.AsyncCheckoutResource
    customers: resources.AsyncCustomersResource
    disputes: resources.AsyncDisputesResource
    payments: resources.AsyncPaymentsResource
    payouts: resources.AsyncPayoutsResource
    products: resources.AsyncProductsResource
    refunds: resources.AsyncRefundsResource
    subscriptions: resources.AsyncSubscriptionsResource
    webhook_events: resources.AsyncWebhookEventsResource
    outgoing_webhooks: resources.AsyncOutgoingWebhooksResource
    with_raw_response: AsyncDodoPaymentsWithRawResponse
    with_streaming_response: AsyncDodoPaymentsWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async dodo-payments client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise DodoPaymentsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("DODO_PAYMENTS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `DODO_PAYMENTS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.checkout = resources.AsyncCheckoutResource(self)
        self.customers = resources.AsyncCustomersResource(self)
        self.disputes = resources.AsyncDisputesResource(self)
        self.payments = resources.AsyncPaymentsResource(self)
        self.payouts = resources.AsyncPayoutsResource(self)
        self.products = resources.AsyncProductsResource(self)
        self.refunds = resources.AsyncRefundsResource(self)
        self.subscriptions = resources.AsyncSubscriptionsResource(self)
        self.webhook_events = resources.AsyncWebhookEventsResource(self)
        self.outgoing_webhooks = resources.AsyncOutgoingWebhooksResource(self)
        self.with_raw_response = AsyncDodoPaymentsWithRawResponse(self)
        self.with_streaming_response = AsyncDodoPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DodoPaymentsWithRawResponse:
    def __init__(self, client: DodoPayments) -> None:
        self.checkout = resources.CheckoutResourceWithRawResponse(client.checkout)
        self.customers = resources.CustomersResourceWithRawResponse(client.customers)
        self.disputes = resources.DisputesResourceWithRawResponse(client.disputes)
        self.payments = resources.PaymentsResourceWithRawResponse(client.payments)
        self.payouts = resources.PayoutsResourceWithRawResponse(client.payouts)
        self.products = resources.ProductsResourceWithRawResponse(client.products)
        self.refunds = resources.RefundsResourceWithRawResponse(client.refunds)
        self.subscriptions = resources.SubscriptionsResourceWithRawResponse(client.subscriptions)
        self.webhook_events = resources.WebhookEventsResourceWithRawResponse(client.webhook_events)
        self.outgoing_webhooks = resources.OutgoingWebhooksResourceWithRawResponse(client.outgoing_webhooks)


class AsyncDodoPaymentsWithRawResponse:
    def __init__(self, client: AsyncDodoPayments) -> None:
        self.checkout = resources.AsyncCheckoutResourceWithRawResponse(client.checkout)
        self.customers = resources.AsyncCustomersResourceWithRawResponse(client.customers)
        self.disputes = resources.AsyncDisputesResourceWithRawResponse(client.disputes)
        self.payments = resources.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.payouts = resources.AsyncPayoutsResourceWithRawResponse(client.payouts)
        self.products = resources.AsyncProductsResourceWithRawResponse(client.products)
        self.refunds = resources.AsyncRefundsResourceWithRawResponse(client.refunds)
        self.subscriptions = resources.AsyncSubscriptionsResourceWithRawResponse(client.subscriptions)
        self.webhook_events = resources.AsyncWebhookEventsResourceWithRawResponse(client.webhook_events)
        self.outgoing_webhooks = resources.AsyncOutgoingWebhooksResourceWithRawResponse(client.outgoing_webhooks)


class DodoPaymentsWithStreamedResponse:
    def __init__(self, client: DodoPayments) -> None:
        self.checkout = resources.CheckoutResourceWithStreamingResponse(client.checkout)
        self.customers = resources.CustomersResourceWithStreamingResponse(client.customers)
        self.disputes = resources.DisputesResourceWithStreamingResponse(client.disputes)
        self.payments = resources.PaymentsResourceWithStreamingResponse(client.payments)
        self.payouts = resources.PayoutsResourceWithStreamingResponse(client.payouts)
        self.products = resources.ProductsResourceWithStreamingResponse(client.products)
        self.refunds = resources.RefundsResourceWithStreamingResponse(client.refunds)
        self.subscriptions = resources.SubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.webhook_events = resources.WebhookEventsResourceWithStreamingResponse(client.webhook_events)
        self.outgoing_webhooks = resources.OutgoingWebhooksResourceWithStreamingResponse(client.outgoing_webhooks)


class AsyncDodoPaymentsWithStreamedResponse:
    def __init__(self, client: AsyncDodoPayments) -> None:
        self.checkout = resources.AsyncCheckoutResourceWithStreamingResponse(client.checkout)
        self.customers = resources.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.disputes = resources.AsyncDisputesResourceWithStreamingResponse(client.disputes)
        self.payments = resources.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.payouts = resources.AsyncPayoutsResourceWithStreamingResponse(client.payouts)
        self.products = resources.AsyncProductsResourceWithStreamingResponse(client.products)
        self.refunds = resources.AsyncRefundsResourceWithStreamingResponse(client.refunds)
        self.subscriptions = resources.AsyncSubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.webhook_events = resources.AsyncWebhookEventsResourceWithStreamingResponse(client.webhook_events)
        self.outgoing_webhooks = resources.AsyncOutgoingWebhooksResourceWithStreamingResponse(client.outgoing_webhooks)


Client = DodoPayments

AsyncClient = AsyncDodoPayments
