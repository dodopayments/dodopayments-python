# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.customers import EmailBody, EmailLogItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        email = client.customers.emails.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        email = client.customers.emails.list(
            customer_id="customer_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.customers.emails.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.customers.emails.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.emails.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_retrieve_body(self, client: DodoPayments) -> None:
        email = client.customers.emails.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        )
        assert_matches_type(EmailBody, email, path=["response"])

    @parametrize
    def test_raw_response_retrieve_body(self, client: DodoPayments) -> None:
        response = client.customers.emails.with_raw_response.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailBody, email, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_body(self, client: DodoPayments) -> None:
        with client.customers.emails.with_streaming_response.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailBody, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_body(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.emails.with_raw_response.retrieve_body(
                email_log_id="email_log_id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_log_id` but received ''"):
            client.customers.emails.with_raw_response.retrieve_body(
                email_log_id="",
                customer_id="customer_id",
            )


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        email = await async_client.customers.emails.list(
            customer_id="customer_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        email = await async_client.customers.emails.list(
            customer_id="customer_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.customers.emails.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.customers.emails.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[EmailLogItem], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.emails.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_retrieve_body(self, async_client: AsyncDodoPayments) -> None:
        email = await async_client.customers.emails.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        )
        assert_matches_type(EmailBody, email, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_body(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.customers.emails.with_raw_response.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailBody, email, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_body(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.customers.emails.with_streaming_response.retrieve_body(
            email_log_id="email_log_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailBody, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_body(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.emails.with_raw_response.retrieve_body(
                email_log_id="email_log_id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_log_id` but received ''"):
            await async_client.customers.emails.with_raw_response.retrieve_body(
                email_log_id="",
                customer_id="customer_id",
            )
