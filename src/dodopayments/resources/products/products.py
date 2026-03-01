# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...types import (
    TaxCategory,
    product_list_params,
    product_create_params,
    product_update_params,
    product_update_files_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .short_links import (
    ShortLinksResource,
    AsyncShortLinksResource,
    ShortLinksResourceWithRawResponse,
    AsyncShortLinksResourceWithRawResponse,
    ShortLinksResourceWithStreamingResponse,
    AsyncShortLinksResourceWithStreamingResponse,
)
from ...pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.product import Product
from ...types.price_param import PriceParam
from ...types.tax_category import TaxCategory
from ...types.product_list_response import ProductListResponse
from ...types.license_key_duration_param import LicenseKeyDurationParam
from ...types.product_update_files_response import ProductUpdateFilesResponse
from ...types.attach_credit_entitlement_param import AttachCreditEntitlementParam

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def short_links(self) -> ShortLinksResource:
        return ShortLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        price: PriceParam,
        tax_category: TaxCategory,
        addons: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_id: Optional[str] | Omit = omit,
        credit_entitlements: Optional[Iterable[AttachCreditEntitlementParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        digital_product_delivery: Optional[product_create_params.DigitalProductDelivery] | Omit = omit,
        license_key_activation_message: Optional[str] | Omit = omit,
        license_key_activations_limit: Optional[int] | Omit = omit,
        license_key_duration: Optional[LicenseKeyDurationParam] | Omit = omit,
        license_key_enabled: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Args:
          name: Name of the product

          price: Price configuration for the product

          tax_category: Tax category applied to this product

          addons: Addons available for subscription product

          brand_id: Brand id for the product, if not provided will default to primary brand

          credit_entitlements: Optional credit entitlements to attach (max 3)

          description: Optional description of the product

          digital_product_delivery: Choose how you would like you digital product delivered

          license_key_activation_message: Optional message displayed during license key activation

          license_key_activations_limit: The number of times the license key can be activated. Must be 0 or greater

          license_key_duration: Duration configuration for the license key. Set to null if you don't want the
              license key to expire. For subscriptions, the lifetime of the license key is
              tied to the subscription period

          license_key_enabled: When true, generates and sends a license key to your customer. Defaults to false

          metadata: Additional metadata for the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/products",
            body=maybe_transform(
                {
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                    "addons": addons,
                    "brand_id": brand_id,
                    "credit_entitlements": credit_entitlements,
                    "description": description,
                    "digital_product_delivery": digital_product_delivery,
                    "license_key_activation_message": license_key_activation_message,
                    "license_key_activations_limit": license_key_activations_limit,
                    "license_key_duration": license_key_duration,
                    "license_key_enabled": license_key_enabled,
                    "metadata": metadata,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def update(
        self,
        id: str,
        *,
        addons: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_id: Optional[str] | Omit = omit,
        credit_entitlements: Optional[Iterable[AttachCreditEntitlementParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        digital_product_delivery: Optional[product_update_params.DigitalProductDelivery] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        license_key_activation_message: Optional[str] | Omit = omit,
        license_key_activations_limit: Optional[int] | Omit = omit,
        license_key_duration: Optional[LicenseKeyDurationParam] | Omit = omit,
        license_key_enabled: Optional[bool] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        price: Optional[PriceParam] | Omit = omit,
        tax_category: Optional[TaxCategory] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          addons: Available Addons for subscription products

          credit_entitlements: Credit entitlements to update (replaces all existing when present) Send empty
              array to remove all, omit field to leave unchanged

          description: Description of the product, optional and must be at most 1000 characters.

          digital_product_delivery: Choose how you would like you digital product delivered

          image_id: Product image id after its uploaded to S3

          license_key_activation_message: Message sent to the customer upon license key activation.

              Only applicable if `license_key_enabled` is `true`. This message contains
              instructions for activating the license key.

          license_key_activations_limit: Limit for the number of activations for the license key.

              Only applicable if `license_key_enabled` is `true`. Represents the maximum
              number of times the license key can be activated.

          license_key_duration: Duration of the license key if enabled.

              Only applicable if `license_key_enabled` is `true`. Represents the duration in
              days for which the license key is valid.

          license_key_enabled: Whether the product requires a license key.

              If `true`, additional fields related to license key (duration, activations
              limit, activation message) become applicable.

          metadata: Additional metadata for the product

          name: Name of the product, optional and must be at most 100 characters.

          price: Price details of the product.

          tax_category: Tax category of the product.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/products/{id}",
            body=maybe_transform(
                {
                    "addons": addons,
                    "brand_id": brand_id,
                    "credit_entitlements": credit_entitlements,
                    "description": description,
                    "digital_product_delivery": digital_product_delivery,
                    "image_id": image_id,
                    "license_key_activation_message": license_key_activation_message,
                    "license_key_activations_limit": license_key_activations_limit,
                    "license_key_duration": license_key_duration,
                    "license_key_enabled": license_key_enabled,
                    "metadata": metadata,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        brand_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        recurring: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[ProductListResponse]:
        """
        Args:
          archived: List archived products

          brand_id: filter by Brand id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          recurring:
              Filter products by pricing type:

              - `true`: Show only recurring pricing products (e.g. subscriptions)
              - `false`: Show only one-time price products
              - `null` or absent: Show both types of products

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products",
            page=SyncDefaultPageNumberPagination[ProductListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "brand_id": brand_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "recurring": recurring,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/products/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_files(
        self,
        id: str,
        *,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductUpdateFilesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/products/{id}/files",
            body=maybe_transform({"file_name": file_name}, product_update_files_params.ProductUpdateFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateFilesResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def short_links(self) -> AsyncShortLinksResource:
        return AsyncShortLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        price: PriceParam,
        tax_category: TaxCategory,
        addons: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_id: Optional[str] | Omit = omit,
        credit_entitlements: Optional[Iterable[AttachCreditEntitlementParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        digital_product_delivery: Optional[product_create_params.DigitalProductDelivery] | Omit = omit,
        license_key_activation_message: Optional[str] | Omit = omit,
        license_key_activations_limit: Optional[int] | Omit = omit,
        license_key_duration: Optional[LicenseKeyDurationParam] | Omit = omit,
        license_key_enabled: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Args:
          name: Name of the product

          price: Price configuration for the product

          tax_category: Tax category applied to this product

          addons: Addons available for subscription product

          brand_id: Brand id for the product, if not provided will default to primary brand

          credit_entitlements: Optional credit entitlements to attach (max 3)

          description: Optional description of the product

          digital_product_delivery: Choose how you would like you digital product delivered

          license_key_activation_message: Optional message displayed during license key activation

          license_key_activations_limit: The number of times the license key can be activated. Must be 0 or greater

          license_key_duration: Duration configuration for the license key. Set to null if you don't want the
              license key to expire. For subscriptions, the lifetime of the license key is
              tied to the subscription period

          license_key_enabled: When true, generates and sends a license key to your customer. Defaults to false

          metadata: Additional metadata for the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/products",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                    "addons": addons,
                    "brand_id": brand_id,
                    "credit_entitlements": credit_entitlements,
                    "description": description,
                    "digital_product_delivery": digital_product_delivery,
                    "license_key_activation_message": license_key_activation_message,
                    "license_key_activations_limit": license_key_activations_limit,
                    "license_key_duration": license_key_duration,
                    "license_key_enabled": license_key_enabled,
                    "metadata": metadata,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def update(
        self,
        id: str,
        *,
        addons: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_id: Optional[str] | Omit = omit,
        credit_entitlements: Optional[Iterable[AttachCreditEntitlementParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        digital_product_delivery: Optional[product_update_params.DigitalProductDelivery] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        license_key_activation_message: Optional[str] | Omit = omit,
        license_key_activations_limit: Optional[int] | Omit = omit,
        license_key_duration: Optional[LicenseKeyDurationParam] | Omit = omit,
        license_key_enabled: Optional[bool] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        price: Optional[PriceParam] | Omit = omit,
        tax_category: Optional[TaxCategory] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          addons: Available Addons for subscription products

          credit_entitlements: Credit entitlements to update (replaces all existing when present) Send empty
              array to remove all, omit field to leave unchanged

          description: Description of the product, optional and must be at most 1000 characters.

          digital_product_delivery: Choose how you would like you digital product delivered

          image_id: Product image id after its uploaded to S3

          license_key_activation_message: Message sent to the customer upon license key activation.

              Only applicable if `license_key_enabled` is `true`. This message contains
              instructions for activating the license key.

          license_key_activations_limit: Limit for the number of activations for the license key.

              Only applicable if `license_key_enabled` is `true`. Represents the maximum
              number of times the license key can be activated.

          license_key_duration: Duration of the license key if enabled.

              Only applicable if `license_key_enabled` is `true`. Represents the duration in
              days for which the license key is valid.

          license_key_enabled: Whether the product requires a license key.

              If `true`, additional fields related to license key (duration, activations
              limit, activation message) become applicable.

          metadata: Additional metadata for the product

          name: Name of the product, optional and must be at most 100 characters.

          price: Price details of the product.

          tax_category: Tax category of the product.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/products/{id}",
            body=await async_maybe_transform(
                {
                    "addons": addons,
                    "brand_id": brand_id,
                    "credit_entitlements": credit_entitlements,
                    "description": description,
                    "digital_product_delivery": digital_product_delivery,
                    "image_id": image_id,
                    "license_key_activation_message": license_key_activation_message,
                    "license_key_activations_limit": license_key_activations_limit,
                    "license_key_duration": license_key_duration,
                    "license_key_enabled": license_key_enabled,
                    "metadata": metadata,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        brand_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        recurring: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductListResponse, AsyncDefaultPageNumberPagination[ProductListResponse]]:
        """
        Args:
          archived: List archived products

          brand_id: filter by Brand id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          recurring:
              Filter products by pricing type:

              - `true`: Show only recurring pricing products (e.g. subscriptions)
              - `false`: Show only one-time price products
              - `null` or absent: Show both types of products

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products",
            page=AsyncDefaultPageNumberPagination[ProductListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "brand_id": brand_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "recurring": recurring,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/products/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_files(
        self,
        id: str,
        *,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductUpdateFilesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/products/{id}/files",
            body=await async_maybe_transform(
                {"file_name": file_name}, product_update_files_params.ProductUpdateFilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateFilesResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = to_raw_response_wrapper(
            products.update,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.archive = to_raw_response_wrapper(
            products.archive,
        )
        self.unarchive = to_raw_response_wrapper(
            products.unarchive,
        )
        self.update_files = to_raw_response_wrapper(
            products.update_files,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._products.images)

    @cached_property
    def short_links(self) -> ShortLinksResourceWithRawResponse:
        return ShortLinksResourceWithRawResponse(self._products.short_links)


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            products.update,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.archive = async_to_raw_response_wrapper(
            products.archive,
        )
        self.unarchive = async_to_raw_response_wrapper(
            products.unarchive,
        )
        self.update_files = async_to_raw_response_wrapper(
            products.update_files,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._products.images)

    @cached_property
    def short_links(self) -> AsyncShortLinksResourceWithRawResponse:
        return AsyncShortLinksResourceWithRawResponse(self._products.short_links)


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            products.update,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.archive = to_streamed_response_wrapper(
            products.archive,
        )
        self.unarchive = to_streamed_response_wrapper(
            products.unarchive,
        )
        self.update_files = to_streamed_response_wrapper(
            products.update_files,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._products.images)

    @cached_property
    def short_links(self) -> ShortLinksResourceWithStreamingResponse:
        return ShortLinksResourceWithStreamingResponse(self._products.short_links)


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            products.update,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            products.archive,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            products.unarchive,
        )
        self.update_files = async_to_streamed_response_wrapper(
            products.update_files,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._products.images)

    @cached_property
    def short_links(self) -> AsyncShortLinksResourceWithStreamingResponse:
        return AsyncShortLinksResourceWithStreamingResponse(self._products.short_links)
