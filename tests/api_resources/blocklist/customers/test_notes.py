# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types.blocklist.customers import BlockedCustomerNote

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        note = client.blocklist.customers.notes.create(
            entry_id="entry_id",
            note="note",
        )
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.notes.with_raw_response.create(
            entry_id="entry_id",
            note="note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.blocklist.customers.notes.with_streaming_response.create(
            entry_id="entry_id",
            note="note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(BlockedCustomerNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.blocklist.customers.notes.with_raw_response.create(
                entry_id="",
                note="note",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        note = client.blocklist.customers.notes.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        )
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.notes.with_raw_response.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.blocklist.customers.notes.with_streaming_response.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(BlockedCustomerNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.blocklist.customers.notes.with_raw_response.update(
                note_id="note_id",
                entry_id="",
                note="note",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            client.blocklist.customers.notes.with_raw_response.update(
                note_id="",
                entry_id="entry_id",
                note="note",
            )


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        note = await async_client.blocklist.customers.notes.create(
            entry_id="entry_id",
            note="note",
        )
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.notes.with_raw_response.create(
            entry_id="entry_id",
            note="note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.notes.with_streaming_response.create(
            entry_id="entry_id",
            note="note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(BlockedCustomerNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.blocklist.customers.notes.with_raw_response.create(
                entry_id="",
                note="note",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        note = await async_client.blocklist.customers.notes.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        )
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.notes.with_raw_response.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(BlockedCustomerNote, note, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.notes.with_streaming_response.update(
            note_id="note_id",
            entry_id="entry_id",
            note="note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(BlockedCustomerNote, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.blocklist.customers.notes.with_raw_response.update(
                note_id="note_id",
                entry_id="",
                note="note",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `note_id` but received ''"):
            await async_client.blocklist.customers.notes.with_raw_response.update(
                note_id="",
                entry_id="entry_id",
                note="note",
            )
