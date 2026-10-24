# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import Locale
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.addons import translation_list_params, translation_update_params
from ...types.locale import Locale
from ...types.products.translation import Translation
from ...types.products.translations_list_response import TranslationsListResponse

__all__ = ["TranslationsResource", "AsyncTranslationsResource"]


class TranslationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return TranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return TranslationsResourceWithStreamingResponse(self)

    def update(
        self,
        locale: Locale,
        *,
        id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Translation:
        """Creates or replaces the translation of one locale.

        The response is 201 for a new
        locale and 200 for a replaced locale.

        Args:
          locale: A locale that the checkout and the customer portal can show.

              The codes are a copy of the checkout locales. `GET /locales` lists them.

          description: The translated description.

          name: The translated name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        return self._put(
            path_template("/addons/{id}/translations/{locale}", id=id, locale=locale),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                translation_update_params.TranslationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Translation,
        )

    def list(
        self,
        id: str,
        *,
        locale: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationsListResponse:
        """
        Lists the translations, for all the locales or for the locales of the filter.

        Args:
          locale: Returns only these locales, for example `?locale=fr&locale=de`. With no value,
              the response has all the locales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/addons/{id}/translations", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"locale": locale}, translation_list_params.TranslationListParams),
            ),
            cast_to=TranslationsListResponse,
        )

    def delete(
        self,
        locale: Locale,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the translation of one locale.

        Args:
          locale: A locale that the checkout and the customer portal can show.

              The codes are a copy of the checkout locales. `GET /locales` lists them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/addons/{id}/translations/{locale}", id=id, locale=locale),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTranslationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncTranslationsResourceWithStreamingResponse(self)

    async def update(
        self,
        locale: Locale,
        *,
        id: str,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Translation:
        """Creates or replaces the translation of one locale.

        The response is 201 for a new
        locale and 200 for a replaced locale.

        Args:
          locale: A locale that the checkout and the customer portal can show.

              The codes are a copy of the checkout locales. `GET /locales` lists them.

          description: The translated description.

          name: The translated name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        return await self._put(
            path_template("/addons/{id}/translations/{locale}", id=id, locale=locale),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                translation_update_params.TranslationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Translation,
        )

    async def list(
        self,
        id: str,
        *,
        locale: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationsListResponse:
        """
        Lists the translations, for all the locales or for the locales of the filter.

        Args:
          locale: Returns only these locales, for example `?locale=fr&locale=de`. With no value,
              the response has all the locales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/addons/{id}/translations", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"locale": locale}, translation_list_params.TranslationListParams),
            ),
            cast_to=TranslationsListResponse,
        )

    async def delete(
        self,
        locale: Locale,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the translation of one locale.

        Args:
          locale: A locale that the checkout and the customer portal can show.

              The codes are a copy of the checkout locales. `GET /locales` lists them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/addons/{id}/translations/{locale}", id=id, locale=locale),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TranslationsResourceWithRawResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.update = to_raw_response_wrapper(
            translations.update,
        )
        self.list = to_raw_response_wrapper(
            translations.list,
        )
        self.delete = to_raw_response_wrapper(
            translations.delete,
        )


class AsyncTranslationsResourceWithRawResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.update = async_to_raw_response_wrapper(
            translations.update,
        )
        self.list = async_to_raw_response_wrapper(
            translations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            translations.delete,
        )


class TranslationsResourceWithStreamingResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.update = to_streamed_response_wrapper(
            translations.update,
        )
        self.list = to_streamed_response_wrapper(
            translations.list,
        )
        self.delete = to_streamed_response_wrapper(
            translations.delete,
        )


class AsyncTranslationsResourceWithStreamingResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.update = async_to_streamed_response_wrapper(
            translations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            translations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            translations.delete,
        )
