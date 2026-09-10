# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.customers import email_list_params
from ...types.customers.email_body import EmailBody
from ...types.customers.email_log_item import EmailLogItem

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[EmailLogItem]:
        """
        Returns every transactional email sent to this customer in the last 180 days,
        newest first, with its delivery outcome. Delivery status comes from the email
        provider and is as fresh as replication, typically seconds.

        Args:
          page_number: Which page to return. The default is 0.

          page_size: How many emails to return. The default is 10 and the maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            path_template("/customers/{customer_id}/emails", customer_id=customer_id),
            page=SyncDefaultPageNumberPagination[EmailLogItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            model=EmailLogItem,
        )

    def retrieve_body(
        self,
        email_log_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBody:
        """
        Returns the email exactly as it was sent, plus the reason it failed when it did.
        Some emails have no body to show: an authentication email carries a live login
        token, a blocked email never reached the provider, and the provider clears
        bodies at 180 days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not email_log_id:
            raise ValueError(f"Expected a non-empty value for `email_log_id` but received {email_log_id!r}")
        return self._get(
            path_template(
                "/customers/{customer_id}/emails/{email_log_id}/body",
                customer_id=customer_id,
                email_log_id=email_log_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBody,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailLogItem, AsyncDefaultPageNumberPagination[EmailLogItem]]:
        """
        Returns every transactional email sent to this customer in the last 180 days,
        newest first, with its delivery outcome. Delivery status comes from the email
        provider and is as fresh as replication, typically seconds.

        Args:
          page_number: Which page to return. The default is 0.

          page_size: How many emails to return. The default is 10 and the maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            path_template("/customers/{customer_id}/emails", customer_id=customer_id),
            page=AsyncDefaultPageNumberPagination[EmailLogItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            model=EmailLogItem,
        )

    async def retrieve_body(
        self,
        email_log_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBody:
        """
        Returns the email exactly as it was sent, plus the reason it failed when it did.
        Some emails have no body to show: an authentication email carries a live login
        token, a blocked email never reached the provider, and the provider clears
        bodies at 180 days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not email_log_id:
            raise ValueError(f"Expected a non-empty value for `email_log_id` but received {email_log_id!r}")
        return await self._get(
            path_template(
                "/customers/{customer_id}/emails/{email_log_id}/body",
                customer_id=customer_id,
                email_log_id=email_log_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBody,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.list = to_raw_response_wrapper(
            emails.list,
        )
        self.retrieve_body = to_raw_response_wrapper(
            emails.retrieve_body,
        )


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.list = async_to_raw_response_wrapper(
            emails.list,
        )
        self.retrieve_body = async_to_raw_response_wrapper(
            emails.retrieve_body,
        )


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.list = to_streamed_response_wrapper(
            emails.list,
        )
        self.retrieve_body = to_streamed_response_wrapper(
            emails.retrieve_body,
        )


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.list = async_to_streamed_response_wrapper(
            emails.list,
        )
        self.retrieve_body = async_to_streamed_response_wrapper(
            emails.retrieve_body,
        )
