# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import moderation_screen_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.moderation_screen_response import ModerationScreenResponse
from ..types.moderation_retrieve_usage_response import ModerationRetrieveUsageResponse

__all__ = ["ModerationResource", "AsyncModerationResource"]


class ModerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return ModerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return ModerationResourceWithStreamingResponse(self)

    def retrieve_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerationRetrieveUsageResponse:
        """
        Shows how many billable screens you made and how close you are to your next
        charge.

        **Billing.** A billable screen is a live-mode screen that returns a verdict.
        Dodo Payments charges $0.30 for each full block of 1000 billable screens and
        debits the fee from your balance. Each full block is charged within one hour.
        Screens that do not fill a block stay unbilled until they do. Errors and
        test-mode screens are free and are not counted.
        """
        return self._get(
            "/moderation/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationRetrieveUsageResponse,
        )

    def screen(
        self,
        *,
        image: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerationScreenResponse:
        """
        Screens text, an image, or both, and returns a verdict: `allow`, `flag` or
        `deny`. The API is fail-closed: do not generate when you get no verdict.

        **Pricing.** Dodo Payments charges $0.30 per 1000 billable screens and debits
        the fee from your balance. A billable screen is a live-mode screen that returns
        a verdict. Errors and test-mode screens are free.

        **429.** Honour `Retry-After` and retry. A 429 is a throughput limit, not a
        verdict.

        **Test mode** returns mock verdicts and never calls the model. The default
        verdict is `allow`. Put one of these strings in `text` to select another
        outcome: `dodo_mock_flag` (`flag`), `dodo_mock_deny` (`deny`),
        `dodo_mock_overloaded` (429) or `dodo_mock_not_ready` (503).

        Args:
          image: The image to screen, as base64, with or without a `data:image/...;base64,`
              prefix. The formats are JPEG, PNG, WebP, GIF and BMP. The limit is 6991530
              base64 characters, and the decoded image must be at most 5 MiB.

          request_id: Your identifier for this screen, up to 128 characters, with no control
              characters. The response returns it in `request_id`.

          text: The text to screen, up to 8000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/moderation/screen",
            body=maybe_transform(
                {
                    "image": image,
                    "request_id": request_id,
                    "text": text,
                },
                moderation_screen_params.ModerationScreenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationScreenResponse,
        )


class AsyncModerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncModerationResourceWithStreamingResponse(self)

    async def retrieve_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerationRetrieveUsageResponse:
        """
        Shows how many billable screens you made and how close you are to your next
        charge.

        **Billing.** A billable screen is a live-mode screen that returns a verdict.
        Dodo Payments charges $0.30 for each full block of 1000 billable screens and
        debits the fee from your balance. Each full block is charged within one hour.
        Screens that do not fill a block stay unbilled until they do. Errors and
        test-mode screens are free and are not counted.
        """
        return await self._get(
            "/moderation/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationRetrieveUsageResponse,
        )

    async def screen(
        self,
        *,
        image: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModerationScreenResponse:
        """
        Screens text, an image, or both, and returns a verdict: `allow`, `flag` or
        `deny`. The API is fail-closed: do not generate when you get no verdict.

        **Pricing.** Dodo Payments charges $0.30 per 1000 billable screens and debits
        the fee from your balance. A billable screen is a live-mode screen that returns
        a verdict. Errors and test-mode screens are free.

        **429.** Honour `Retry-After` and retry. A 429 is a throughput limit, not a
        verdict.

        **Test mode** returns mock verdicts and never calls the model. The default
        verdict is `allow`. Put one of these strings in `text` to select another
        outcome: `dodo_mock_flag` (`flag`), `dodo_mock_deny` (`deny`),
        `dodo_mock_overloaded` (429) or `dodo_mock_not_ready` (503).

        Args:
          image: The image to screen, as base64, with or without a `data:image/...;base64,`
              prefix. The formats are JPEG, PNG, WebP, GIF and BMP. The limit is 6991530
              base64 characters, and the decoded image must be at most 5 MiB.

          request_id: Your identifier for this screen, up to 128 characters, with no control
              characters. The response returns it in `request_id`.

          text: The text to screen, up to 8000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/moderation/screen",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "request_id": request_id,
                    "text": text,
                },
                moderation_screen_params.ModerationScreenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModerationScreenResponse,
        )


class ModerationResourceWithRawResponse:
    def __init__(self, moderation: ModerationResource) -> None:
        self._moderation = moderation

        self.retrieve_usage = to_raw_response_wrapper(
            moderation.retrieve_usage,
        )
        self.screen = to_raw_response_wrapper(
            moderation.screen,
        )


class AsyncModerationResourceWithRawResponse:
    def __init__(self, moderation: AsyncModerationResource) -> None:
        self._moderation = moderation

        self.retrieve_usage = async_to_raw_response_wrapper(
            moderation.retrieve_usage,
        )
        self.screen = async_to_raw_response_wrapper(
            moderation.screen,
        )


class ModerationResourceWithStreamingResponse:
    def __init__(self, moderation: ModerationResource) -> None:
        self._moderation = moderation

        self.retrieve_usage = to_streamed_response_wrapper(
            moderation.retrieve_usage,
        )
        self.screen = to_streamed_response_wrapper(
            moderation.screen,
        )


class AsyncModerationResourceWithStreamingResponse:
    def __init__(self, moderation: AsyncModerationResource) -> None:
        self._moderation = moderation

        self.retrieve_usage = async_to_streamed_response_wrapper(
            moderation.retrieve_usage,
        )
        self.screen = async_to_streamed_response_wrapper(
            moderation.screen,
        )
