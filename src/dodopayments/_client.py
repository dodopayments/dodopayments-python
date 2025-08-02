# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
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
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    misc,
    addons,
    brands,
    payouts,
    refunds,
    disputes,
    licenses,
    payments,
    discounts,
    license_keys,
    subscriptions,
    license_key_instances,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, DodoPaymentsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.invoices import invoices
from .resources.products import products
from .resources.customers import customers

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
    payments: payments.PaymentsResource
    subscriptions: subscriptions.SubscriptionsResource
    invoices: invoices.InvoicesResource
    licenses: licenses.LicensesResource
    license_keys: license_keys.LicenseKeysResource
    license_key_instances: license_key_instances.LicenseKeyInstancesResource
    customers: customers.CustomersResource
    refunds: refunds.RefundsResource
    disputes: disputes.DisputesResource
    payouts: payouts.PayoutsResource
    products: products.ProductsResource
    misc: misc.MiscResource
    discounts: discounts.DiscountsResource
    addons: addons.AddonsResource
    brands: brands.BrandsResource
    with_raw_response: DodoPaymentsWithRawResponse
    with_streaming_response: DodoPaymentsWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["live_mode", "test_mode"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["live_mode", "test_mode"] | NotGiven = NOT_GIVEN,
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
        """Construct a new synchronous DodoPayments client instance.

        This automatically infers the `bearer_token` argument from the `DODO_PAYMENTS_API_KEY` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("DODO_PAYMENTS_API_KEY")
        if bearer_token is None:
            raise DodoPaymentsError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the DODO_PAYMENTS_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

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

        self.payments = payments.PaymentsResource(self)
        self.subscriptions = subscriptions.SubscriptionsResource(self)
        self.invoices = invoices.InvoicesResource(self)
        self.licenses = licenses.LicensesResource(self)
        self.license_keys = license_keys.LicenseKeysResource(self)
        self.license_key_instances = license_key_instances.LicenseKeyInstancesResource(self)
        self.customers = customers.CustomersResource(self)
        self.refunds = refunds.RefundsResource(self)
        self.disputes = disputes.DisputesResource(self)
        self.payouts = payouts.PayoutsResource(self)
        self.products = products.ProductsResource(self)
        self.misc = misc.MiscResource(self)
        self.discounts = discounts.DiscountsResource(self)
        self.addons = addons.AddonsResource(self)
        self.brands = brands.BrandsResource(self)
        self.with_raw_response = DodoPaymentsWithRawResponse(self)
        self.with_streaming_response = DodoPaymentsWithStreamedResponse(self)

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
        environment: Literal["live_mode", "test_mode"] | None = None,
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
            bearer_token=bearer_token or self.bearer_token,
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
    payments: payments.AsyncPaymentsResource
    subscriptions: subscriptions.AsyncSubscriptionsResource
    invoices: invoices.AsyncInvoicesResource
    licenses: licenses.AsyncLicensesResource
    license_keys: license_keys.AsyncLicenseKeysResource
    license_key_instances: license_key_instances.AsyncLicenseKeyInstancesResource
    customers: customers.AsyncCustomersResource
    refunds: refunds.AsyncRefundsResource
    disputes: disputes.AsyncDisputesResource
    payouts: payouts.AsyncPayoutsResource
    products: products.AsyncProductsResource
    misc: misc.AsyncMiscResource
    discounts: discounts.AsyncDiscountsResource
    addons: addons.AsyncAddonsResource
    brands: brands.AsyncBrandsResource
    with_raw_response: AsyncDodoPaymentsWithRawResponse
    with_streaming_response: AsyncDodoPaymentsWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["live_mode", "test_mode"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["live_mode", "test_mode"] | NotGiven = NOT_GIVEN,
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
        """Construct a new async AsyncDodoPayments client instance.

        This automatically infers the `bearer_token` argument from the `DODO_PAYMENTS_API_KEY` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("DODO_PAYMENTS_API_KEY")
        if bearer_token is None:
            raise DodoPaymentsError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the DODO_PAYMENTS_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

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

        self.payments = payments.AsyncPaymentsResource(self)
        self.subscriptions = subscriptions.AsyncSubscriptionsResource(self)
        self.invoices = invoices.AsyncInvoicesResource(self)
        self.licenses = licenses.AsyncLicensesResource(self)
        self.license_keys = license_keys.AsyncLicenseKeysResource(self)
        self.license_key_instances = license_key_instances.AsyncLicenseKeyInstancesResource(self)
        self.customers = customers.AsyncCustomersResource(self)
        self.refunds = refunds.AsyncRefundsResource(self)
        self.disputes = disputes.AsyncDisputesResource(self)
        self.payouts = payouts.AsyncPayoutsResource(self)
        self.products = products.AsyncProductsResource(self)
        self.misc = misc.AsyncMiscResource(self)
        self.discounts = discounts.AsyncDiscountsResource(self)
        self.addons = addons.AsyncAddonsResource(self)
        self.brands = brands.AsyncBrandsResource(self)
        self.with_raw_response = AsyncDodoPaymentsWithRawResponse(self)
        self.with_streaming_response = AsyncDodoPaymentsWithStreamedResponse(self)

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
        environment: Literal["live_mode", "test_mode"] | None = None,
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
            bearer_token=bearer_token or self.bearer_token,
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
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)
        self.subscriptions = subscriptions.SubscriptionsResourceWithRawResponse(client.subscriptions)
        self.invoices = invoices.InvoicesResourceWithRawResponse(client.invoices)
        self.licenses = licenses.LicensesResourceWithRawResponse(client.licenses)
        self.license_keys = license_keys.LicenseKeysResourceWithRawResponse(client.license_keys)
        self.license_key_instances = license_key_instances.LicenseKeyInstancesResourceWithRawResponse(
            client.license_key_instances
        )
        self.customers = customers.CustomersResourceWithRawResponse(client.customers)
        self.refunds = refunds.RefundsResourceWithRawResponse(client.refunds)
        self.disputes = disputes.DisputesResourceWithRawResponse(client.disputes)
        self.payouts = payouts.PayoutsResourceWithRawResponse(client.payouts)
        self.products = products.ProductsResourceWithRawResponse(client.products)
        self.misc = misc.MiscResourceWithRawResponse(client.misc)
        self.discounts = discounts.DiscountsResourceWithRawResponse(client.discounts)
        self.addons = addons.AddonsResourceWithRawResponse(client.addons)
        self.brands = brands.BrandsResourceWithRawResponse(client.brands)


class AsyncDodoPaymentsWithRawResponse:
    def __init__(self, client: AsyncDodoPayments) -> None:
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.subscriptions = subscriptions.AsyncSubscriptionsResourceWithRawResponse(client.subscriptions)
        self.invoices = invoices.AsyncInvoicesResourceWithRawResponse(client.invoices)
        self.licenses = licenses.AsyncLicensesResourceWithRawResponse(client.licenses)
        self.license_keys = license_keys.AsyncLicenseKeysResourceWithRawResponse(client.license_keys)
        self.license_key_instances = license_key_instances.AsyncLicenseKeyInstancesResourceWithRawResponse(
            client.license_key_instances
        )
        self.customers = customers.AsyncCustomersResourceWithRawResponse(client.customers)
        self.refunds = refunds.AsyncRefundsResourceWithRawResponse(client.refunds)
        self.disputes = disputes.AsyncDisputesResourceWithRawResponse(client.disputes)
        self.payouts = payouts.AsyncPayoutsResourceWithRawResponse(client.payouts)
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)
        self.misc = misc.AsyncMiscResourceWithRawResponse(client.misc)
        self.discounts = discounts.AsyncDiscountsResourceWithRawResponse(client.discounts)
        self.addons = addons.AsyncAddonsResourceWithRawResponse(client.addons)
        self.brands = brands.AsyncBrandsResourceWithRawResponse(client.brands)


class DodoPaymentsWithStreamedResponse:
    def __init__(self, client: DodoPayments) -> None:
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)
        self.subscriptions = subscriptions.SubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.invoices = invoices.InvoicesResourceWithStreamingResponse(client.invoices)
        self.licenses = licenses.LicensesResourceWithStreamingResponse(client.licenses)
        self.license_keys = license_keys.LicenseKeysResourceWithStreamingResponse(client.license_keys)
        self.license_key_instances = license_key_instances.LicenseKeyInstancesResourceWithStreamingResponse(
            client.license_key_instances
        )
        self.customers = customers.CustomersResourceWithStreamingResponse(client.customers)
        self.refunds = refunds.RefundsResourceWithStreamingResponse(client.refunds)
        self.disputes = disputes.DisputesResourceWithStreamingResponse(client.disputes)
        self.payouts = payouts.PayoutsResourceWithStreamingResponse(client.payouts)
        self.products = products.ProductsResourceWithStreamingResponse(client.products)
        self.misc = misc.MiscResourceWithStreamingResponse(client.misc)
        self.discounts = discounts.DiscountsResourceWithStreamingResponse(client.discounts)
        self.addons = addons.AddonsResourceWithStreamingResponse(client.addons)
        self.brands = brands.BrandsResourceWithStreamingResponse(client.brands)


class AsyncDodoPaymentsWithStreamedResponse:
    def __init__(self, client: AsyncDodoPayments) -> None:
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.subscriptions = subscriptions.AsyncSubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.invoices = invoices.AsyncInvoicesResourceWithStreamingResponse(client.invoices)
        self.licenses = licenses.AsyncLicensesResourceWithStreamingResponse(client.licenses)
        self.license_keys = license_keys.AsyncLicenseKeysResourceWithStreamingResponse(client.license_keys)
        self.license_key_instances = license_key_instances.AsyncLicenseKeyInstancesResourceWithStreamingResponse(
            client.license_key_instances
        )
        self.customers = customers.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.refunds = refunds.AsyncRefundsResourceWithStreamingResponse(client.refunds)
        self.disputes = disputes.AsyncDisputesResourceWithStreamingResponse(client.disputes)
        self.payouts = payouts.AsyncPayoutsResourceWithStreamingResponse(client.payouts)
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)
        self.misc = misc.AsyncMiscResourceWithStreamingResponse(client.misc)
        self.discounts = discounts.AsyncDiscountsResourceWithStreamingResponse(client.discounts)
        self.addons = addons.AsyncAddonsResourceWithStreamingResponse(client.addons)
        self.brands = brands.AsyncBrandsResourceWithStreamingResponse(client.brands)


Client = DodoPayments

AsyncClient = AsyncDodoPayments
