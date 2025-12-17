# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, DodoPaymentsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        misc,
        addons,
        brands,
        meters,
        payouts,
        refunds,
        disputes,
        invoices,
        licenses,
        payments,
        products,
        webhooks,
        customers,
        discounts,
        license_keys,
        usage_events,
        subscriptions,
        checkout_sessions,
        license_key_instances,
    )
    from .resources.misc import MiscResource, AsyncMiscResource
    from .resources.addons import AddonsResource, AsyncAddonsResource
    from .resources.brands import BrandsResource, AsyncBrandsResource
    from .resources.meters import MetersResource, AsyncMetersResource
    from .resources.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.refunds import RefundsResource, AsyncRefundsResource
    from .resources.disputes import DisputesResource, AsyncDisputesResource
    from .resources.licenses import LicensesResource, AsyncLicensesResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.discounts import DiscountsResource, AsyncDiscountsResource
    from .resources.license_keys import LicenseKeysResource, AsyncLicenseKeysResource
    from .resources.usage_events import UsageEventsResource, AsyncUsageEventsResource
    from .resources.subscriptions import SubscriptionsResource, AsyncSubscriptionsResource
    from .resources.checkout_sessions import CheckoutSessionsResource, AsyncCheckoutSessionsResource
    from .resources.invoices.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.products.products import ProductsResource, AsyncProductsResource
    from .resources.webhooks.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.customers.customers import CustomersResource, AsyncCustomersResource
    from .resources.license_key_instances import LicenseKeyInstancesResource, AsyncLicenseKeyInstancesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "DodoPayments",
    "AsyncDodoPayments",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "live_mode": "https://live.dodopayments.com",
    "test_mode": "https://test.dodopayments.com",
}


class DodoPayments(SyncAPIClient):
    # client options
    bearer_token: str
    webhook_key: str | None

    _environment: Literal["live_mode", "test_mode"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_key: str | None = None,
        environment: Literal["live_mode", "test_mode"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous DodoPayments client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `DODO_PAYMENTS_API_KEY`
        - `webhook_key` from `DODO_PAYMENTS_WEBHOOK_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("DODO_PAYMENTS_API_KEY")
        if bearer_token is None:
            raise DodoPaymentsError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the DODO_PAYMENTS_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

        if webhook_key is None:
            webhook_key = os.environ.get("DODO_PAYMENTS_WEBHOOK_KEY")
        self.webhook_key = webhook_key

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
            self._environment = environment = "live_mode"

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

    @cached_property
    def checkout_sessions(self) -> CheckoutSessionsResource:
        from .resources.checkout_sessions import CheckoutSessionsResource

        return CheckoutSessionsResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        from .resources.subscriptions import SubscriptionsResource

        return SubscriptionsResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def licenses(self) -> LicensesResource:
        from .resources.licenses import LicensesResource

        return LicensesResource(self)

    @cached_property
    def license_keys(self) -> LicenseKeysResource:
        from .resources.license_keys import LicenseKeysResource

        return LicenseKeysResource(self)

    @cached_property
    def license_key_instances(self) -> LicenseKeyInstancesResource:
        from .resources.license_key_instances import LicenseKeyInstancesResource

        return LicenseKeyInstancesResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        from .resources.customers import CustomersResource

        return CustomersResource(self)

    @cached_property
    def refunds(self) -> RefundsResource:
        from .resources.refunds import RefundsResource

        return RefundsResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        from .resources.disputes import DisputesResource

        return DisputesResource(self)

    @cached_property
    def payouts(self) -> PayoutsResource:
        from .resources.payouts import PayoutsResource

        return PayoutsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def misc(self) -> MiscResource:
        from .resources.misc import MiscResource

        return MiscResource(self)

    @cached_property
    def discounts(self) -> DiscountsResource:
        from .resources.discounts import DiscountsResource

        return DiscountsResource(self)

    @cached_property
    def addons(self) -> AddonsResource:
        from .resources.addons import AddonsResource

        return AddonsResource(self)

    @cached_property
    def brands(self) -> BrandsResource:
        from .resources.brands import BrandsResource

        return BrandsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def usage_events(self) -> UsageEventsResource:
        from .resources.usage_events import UsageEventsResource

        return UsageEventsResource(self)

    @cached_property
    def meters(self) -> MetersResource:
        from .resources.meters import MetersResource

        return MetersResource(self)

    @cached_property
    def with_raw_response(self) -> DodoPaymentsWithRawResponse:
        return DodoPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DodoPaymentsWithStreamedResponse:
        return DodoPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

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
        bearer_token: str | None = None,
        webhook_key: str | None = None,
        environment: Literal["live_mode", "test_mode"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            bearer_token=bearer_token or self.bearer_token,
            webhook_key=webhook_key or self.webhook_key,
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
    # client options
    bearer_token: str
    webhook_key: str | None

    _environment: Literal["live_mode", "test_mode"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_key: str | None = None,
        environment: Literal["live_mode", "test_mode"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncDodoPayments client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `DODO_PAYMENTS_API_KEY`
        - `webhook_key` from `DODO_PAYMENTS_WEBHOOK_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("DODO_PAYMENTS_API_KEY")
        if bearer_token is None:
            raise DodoPaymentsError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the DODO_PAYMENTS_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

        if webhook_key is None:
            webhook_key = os.environ.get("DODO_PAYMENTS_WEBHOOK_KEY")
        self.webhook_key = webhook_key

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
            self._environment = environment = "live_mode"

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

    @cached_property
    def checkout_sessions(self) -> AsyncCheckoutSessionsResource:
        from .resources.checkout_sessions import AsyncCheckoutSessionsResource

        return AsyncCheckoutSessionsResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        from .resources.subscriptions import AsyncSubscriptionsResource

        return AsyncSubscriptionsResource(self)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def licenses(self) -> AsyncLicensesResource:
        from .resources.licenses import AsyncLicensesResource

        return AsyncLicensesResource(self)

    @cached_property
    def license_keys(self) -> AsyncLicenseKeysResource:
        from .resources.license_keys import AsyncLicenseKeysResource

        return AsyncLicenseKeysResource(self)

    @cached_property
    def license_key_instances(self) -> AsyncLicenseKeyInstancesResource:
        from .resources.license_key_instances import AsyncLicenseKeyInstancesResource

        return AsyncLicenseKeyInstancesResource(self)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        from .resources.customers import AsyncCustomersResource

        return AsyncCustomersResource(self)

    @cached_property
    def refunds(self) -> AsyncRefundsResource:
        from .resources.refunds import AsyncRefundsResource

        return AsyncRefundsResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        from .resources.disputes import AsyncDisputesResource

        return AsyncDisputesResource(self)

    @cached_property
    def payouts(self) -> AsyncPayoutsResource:
        from .resources.payouts import AsyncPayoutsResource

        return AsyncPayoutsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def misc(self) -> AsyncMiscResource:
        from .resources.misc import AsyncMiscResource

        return AsyncMiscResource(self)

    @cached_property
    def discounts(self) -> AsyncDiscountsResource:
        from .resources.discounts import AsyncDiscountsResource

        return AsyncDiscountsResource(self)

    @cached_property
    def addons(self) -> AsyncAddonsResource:
        from .resources.addons import AsyncAddonsResource

        return AsyncAddonsResource(self)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        from .resources.brands import AsyncBrandsResource

        return AsyncBrandsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def usage_events(self) -> AsyncUsageEventsResource:
        from .resources.usage_events import AsyncUsageEventsResource

        return AsyncUsageEventsResource(self)

    @cached_property
    def meters(self) -> AsyncMetersResource:
        from .resources.meters import AsyncMetersResource

        return AsyncMetersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncDodoPaymentsWithRawResponse:
        return AsyncDodoPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDodoPaymentsWithStreamedResponse:
        return AsyncDodoPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

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
        bearer_token: str | None = None,
        webhook_key: str | None = None,
        environment: Literal["live_mode", "test_mode"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            bearer_token=bearer_token or self.bearer_token,
            webhook_key=webhook_key or self.webhook_key,
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
    _client: DodoPayments

    def __init__(self, client: DodoPayments) -> None:
        self._client = client

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.CheckoutSessionsResourceWithRawResponse:
        from .resources.checkout_sessions import CheckoutSessionsResourceWithRawResponse

        return CheckoutSessionsResourceWithRawResponse(self._client.checkout_sessions)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithRawResponse:
        from .resources.subscriptions import SubscriptionsResourceWithRawResponse

        return SubscriptionsResourceWithRawResponse(self._client.subscriptions)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def licenses(self) -> licenses.LicensesResourceWithRawResponse:
        from .resources.licenses import LicensesResourceWithRawResponse

        return LicensesResourceWithRawResponse(self._client.licenses)

    @cached_property
    def license_keys(self) -> license_keys.LicenseKeysResourceWithRawResponse:
        from .resources.license_keys import LicenseKeysResourceWithRawResponse

        return LicenseKeysResourceWithRawResponse(self._client.license_keys)

    @cached_property
    def license_key_instances(self) -> license_key_instances.LicenseKeyInstancesResourceWithRawResponse:
        from .resources.license_key_instances import LicenseKeyInstancesResourceWithRawResponse

        return LicenseKeyInstancesResourceWithRawResponse(self._client.license_key_instances)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        from .resources.customers import CustomersResourceWithRawResponse

        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithRawResponse:
        from .resources.refunds import RefundsResourceWithRawResponse

        return RefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        from .resources.disputes import DisputesResourceWithRawResponse

        return DisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithRawResponse:
        from .resources.payouts import PayoutsResourceWithRawResponse

        return PayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def misc(self) -> misc.MiscResourceWithRawResponse:
        from .resources.misc import MiscResourceWithRawResponse

        return MiscResourceWithRawResponse(self._client.misc)

    @cached_property
    def discounts(self) -> discounts.DiscountsResourceWithRawResponse:
        from .resources.discounts import DiscountsResourceWithRawResponse

        return DiscountsResourceWithRawResponse(self._client.discounts)

    @cached_property
    def addons(self) -> addons.AddonsResourceWithRawResponse:
        from .resources.addons import AddonsResourceWithRawResponse

        return AddonsResourceWithRawResponse(self._client.addons)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithRawResponse:
        from .resources.brands import BrandsResourceWithRawResponse

        return BrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def usage_events(self) -> usage_events.UsageEventsResourceWithRawResponse:
        from .resources.usage_events import UsageEventsResourceWithRawResponse

        return UsageEventsResourceWithRawResponse(self._client.usage_events)

    @cached_property
    def meters(self) -> meters.MetersResourceWithRawResponse:
        from .resources.meters import MetersResourceWithRawResponse

        return MetersResourceWithRawResponse(self._client.meters)


class AsyncDodoPaymentsWithRawResponse:
    _client: AsyncDodoPayments

    def __init__(self, client: AsyncDodoPayments) -> None:
        self._client = client

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.AsyncCheckoutSessionsResourceWithRawResponse:
        from .resources.checkout_sessions import AsyncCheckoutSessionsResourceWithRawResponse

        return AsyncCheckoutSessionsResourceWithRawResponse(self._client.checkout_sessions)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithRawResponse:
        from .resources.subscriptions import AsyncSubscriptionsResourceWithRawResponse

        return AsyncSubscriptionsResourceWithRawResponse(self._client.subscriptions)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def licenses(self) -> licenses.AsyncLicensesResourceWithRawResponse:
        from .resources.licenses import AsyncLicensesResourceWithRawResponse

        return AsyncLicensesResourceWithRawResponse(self._client.licenses)

    @cached_property
    def license_keys(self) -> license_keys.AsyncLicenseKeysResourceWithRawResponse:
        from .resources.license_keys import AsyncLicenseKeysResourceWithRawResponse

        return AsyncLicenseKeysResourceWithRawResponse(self._client.license_keys)

    @cached_property
    def license_key_instances(self) -> license_key_instances.AsyncLicenseKeyInstancesResourceWithRawResponse:
        from .resources.license_key_instances import AsyncLicenseKeyInstancesResourceWithRawResponse

        return AsyncLicenseKeyInstancesResourceWithRawResponse(self._client.license_key_instances)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        from .resources.customers import AsyncCustomersResourceWithRawResponse

        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithRawResponse:
        from .resources.refunds import AsyncRefundsResourceWithRawResponse

        return AsyncRefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        from .resources.disputes import AsyncDisputesResourceWithRawResponse

        return AsyncDisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithRawResponse:
        from .resources.payouts import AsyncPayoutsResourceWithRawResponse

        return AsyncPayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def misc(self) -> misc.AsyncMiscResourceWithRawResponse:
        from .resources.misc import AsyncMiscResourceWithRawResponse

        return AsyncMiscResourceWithRawResponse(self._client.misc)

    @cached_property
    def discounts(self) -> discounts.AsyncDiscountsResourceWithRawResponse:
        from .resources.discounts import AsyncDiscountsResourceWithRawResponse

        return AsyncDiscountsResourceWithRawResponse(self._client.discounts)

    @cached_property
    def addons(self) -> addons.AsyncAddonsResourceWithRawResponse:
        from .resources.addons import AsyncAddonsResourceWithRawResponse

        return AsyncAddonsResourceWithRawResponse(self._client.addons)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithRawResponse:
        from .resources.brands import AsyncBrandsResourceWithRawResponse

        return AsyncBrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def usage_events(self) -> usage_events.AsyncUsageEventsResourceWithRawResponse:
        from .resources.usage_events import AsyncUsageEventsResourceWithRawResponse

        return AsyncUsageEventsResourceWithRawResponse(self._client.usage_events)

    @cached_property
    def meters(self) -> meters.AsyncMetersResourceWithRawResponse:
        from .resources.meters import AsyncMetersResourceWithRawResponse

        return AsyncMetersResourceWithRawResponse(self._client.meters)


class DodoPaymentsWithStreamedResponse:
    _client: DodoPayments

    def __init__(self, client: DodoPayments) -> None:
        self._client = client

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.CheckoutSessionsResourceWithStreamingResponse:
        from .resources.checkout_sessions import CheckoutSessionsResourceWithStreamingResponse

        return CheckoutSessionsResourceWithStreamingResponse(self._client.checkout_sessions)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithStreamingResponse:
        from .resources.subscriptions import SubscriptionsResourceWithStreamingResponse

        return SubscriptionsResourceWithStreamingResponse(self._client.subscriptions)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def licenses(self) -> licenses.LicensesResourceWithStreamingResponse:
        from .resources.licenses import LicensesResourceWithStreamingResponse

        return LicensesResourceWithStreamingResponse(self._client.licenses)

    @cached_property
    def license_keys(self) -> license_keys.LicenseKeysResourceWithStreamingResponse:
        from .resources.license_keys import LicenseKeysResourceWithStreamingResponse

        return LicenseKeysResourceWithStreamingResponse(self._client.license_keys)

    @cached_property
    def license_key_instances(self) -> license_key_instances.LicenseKeyInstancesResourceWithStreamingResponse:
        from .resources.license_key_instances import LicenseKeyInstancesResourceWithStreamingResponse

        return LicenseKeyInstancesResourceWithStreamingResponse(self._client.license_key_instances)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        from .resources.customers import CustomersResourceWithStreamingResponse

        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithStreamingResponse:
        from .resources.refunds import RefundsResourceWithStreamingResponse

        return RefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        from .resources.disputes import DisputesResourceWithStreamingResponse

        return DisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithStreamingResponse:
        from .resources.payouts import PayoutsResourceWithStreamingResponse

        return PayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def misc(self) -> misc.MiscResourceWithStreamingResponse:
        from .resources.misc import MiscResourceWithStreamingResponse

        return MiscResourceWithStreamingResponse(self._client.misc)

    @cached_property
    def discounts(self) -> discounts.DiscountsResourceWithStreamingResponse:
        from .resources.discounts import DiscountsResourceWithStreamingResponse

        return DiscountsResourceWithStreamingResponse(self._client.discounts)

    @cached_property
    def addons(self) -> addons.AddonsResourceWithStreamingResponse:
        from .resources.addons import AddonsResourceWithStreamingResponse

        return AddonsResourceWithStreamingResponse(self._client.addons)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithStreamingResponse:
        from .resources.brands import BrandsResourceWithStreamingResponse

        return BrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def usage_events(self) -> usage_events.UsageEventsResourceWithStreamingResponse:
        from .resources.usage_events import UsageEventsResourceWithStreamingResponse

        return UsageEventsResourceWithStreamingResponse(self._client.usage_events)

    @cached_property
    def meters(self) -> meters.MetersResourceWithStreamingResponse:
        from .resources.meters import MetersResourceWithStreamingResponse

        return MetersResourceWithStreamingResponse(self._client.meters)


class AsyncDodoPaymentsWithStreamedResponse:
    _client: AsyncDodoPayments

    def __init__(self, client: AsyncDodoPayments) -> None:
        self._client = client

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.AsyncCheckoutSessionsResourceWithStreamingResponse:
        from .resources.checkout_sessions import AsyncCheckoutSessionsResourceWithStreamingResponse

        return AsyncCheckoutSessionsResourceWithStreamingResponse(self._client.checkout_sessions)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithStreamingResponse:
        from .resources.subscriptions import AsyncSubscriptionsResourceWithStreamingResponse

        return AsyncSubscriptionsResourceWithStreamingResponse(self._client.subscriptions)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def licenses(self) -> licenses.AsyncLicensesResourceWithStreamingResponse:
        from .resources.licenses import AsyncLicensesResourceWithStreamingResponse

        return AsyncLicensesResourceWithStreamingResponse(self._client.licenses)

    @cached_property
    def license_keys(self) -> license_keys.AsyncLicenseKeysResourceWithStreamingResponse:
        from .resources.license_keys import AsyncLicenseKeysResourceWithStreamingResponse

        return AsyncLicenseKeysResourceWithStreamingResponse(self._client.license_keys)

    @cached_property
    def license_key_instances(self) -> license_key_instances.AsyncLicenseKeyInstancesResourceWithStreamingResponse:
        from .resources.license_key_instances import AsyncLicenseKeyInstancesResourceWithStreamingResponse

        return AsyncLicenseKeyInstancesResourceWithStreamingResponse(self._client.license_key_instances)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        from .resources.customers import AsyncCustomersResourceWithStreamingResponse

        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithStreamingResponse:
        from .resources.refunds import AsyncRefundsResourceWithStreamingResponse

        return AsyncRefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        from .resources.disputes import AsyncDisputesResourceWithStreamingResponse

        return AsyncDisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithStreamingResponse:
        from .resources.payouts import AsyncPayoutsResourceWithStreamingResponse

        return AsyncPayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def misc(self) -> misc.AsyncMiscResourceWithStreamingResponse:
        from .resources.misc import AsyncMiscResourceWithStreamingResponse

        return AsyncMiscResourceWithStreamingResponse(self._client.misc)

    @cached_property
    def discounts(self) -> discounts.AsyncDiscountsResourceWithStreamingResponse:
        from .resources.discounts import AsyncDiscountsResourceWithStreamingResponse

        return AsyncDiscountsResourceWithStreamingResponse(self._client.discounts)

    @cached_property
    def addons(self) -> addons.AsyncAddonsResourceWithStreamingResponse:
        from .resources.addons import AsyncAddonsResourceWithStreamingResponse

        return AsyncAddonsResourceWithStreamingResponse(self._client.addons)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithStreamingResponse:
        from .resources.brands import AsyncBrandsResourceWithStreamingResponse

        return AsyncBrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def usage_events(self) -> usage_events.AsyncUsageEventsResourceWithStreamingResponse:
        from .resources.usage_events import AsyncUsageEventsResourceWithStreamingResponse

        return AsyncUsageEventsResourceWithStreamingResponse(self._client.usage_events)

    @cached_property
    def meters(self) -> meters.AsyncMetersResourceWithStreamingResponse:
        from .resources.meters import AsyncMetersResourceWithStreamingResponse

        return AsyncMetersResourceWithStreamingResponse(self._client.meters)


Client = DodoPayments

AsyncClient = AsyncDodoPayments
