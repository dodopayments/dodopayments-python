# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import Meter
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        meter = client.meters.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        meter = client.meters.create(
            aggregation={
                "type": "count",
                "key": "key",
            },
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
            description="description",
            filter={
                "clauses": [
                    {
                        "key": "user_id",
                        "operator": "equals",
                        "value": "user123",
                    },
                    {
                        "key": "amount",
                        "operator": "greater_than",
                        "value": 100,
                    },
                ],
                "conjunction": "and",
            },
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.meters.with_raw_response.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.meters.with_streaming_response.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert_matches_type(Meter, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        meter = client.meters.retrieve(
            "id",
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.meters.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.meters.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert_matches_type(Meter, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meters.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        meter = client.meters.list()
        assert_matches_type(SyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        meter = client.meters.list(
            archived=True,
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.meters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.meters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[Meter], meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: DodoPayments) -> None:
        meter = client.meters.archive(
            "id",
        )
        assert meter is None

    @parametrize
    def test_raw_response_archive(self, client: DodoPayments) -> None:
        response = client.meters.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert meter is None

    @parametrize
    def test_streaming_response_archive(self, client: DodoPayments) -> None:
        with client.meters.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert meter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meters.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_unarchive(self, client: DodoPayments) -> None:
        meter = client.meters.unarchive(
            "id",
        )
        assert meter is None

    @parametrize
    def test_raw_response_unarchive(self, client: DodoPayments) -> None:
        response = client.meters.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = response.parse()
        assert meter is None

    @parametrize
    def test_streaming_response_unarchive(self, client: DodoPayments) -> None:
        with client.meters.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = response.parse()
            assert meter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meters.with_raw_response.unarchive(
                "",
            )


class TestAsyncMeters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.create(
            aggregation={
                "type": "count",
                "key": "key",
            },
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
            description="description",
            filter={
                "clauses": [
                    {
                        "key": "user_id",
                        "operator": "equals",
                        "value": "user123",
                    },
                    {
                        "key": "amount",
                        "operator": "greater_than",
                        "value": 100,
                    },
                ],
                "conjunction": "and",
            },
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.meters.with_raw_response.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.meters.with_streaming_response.create(
            aggregation={"type": "count"},
            event_name="event_name",
            measurement_unit="measurement_unit",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert_matches_type(Meter, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.retrieve(
            "id",
        )
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.meters.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert_matches_type(Meter, meter, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.meters.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert_matches_type(Meter, meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meters.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.list(
            archived=True,
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.meters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[Meter], meter, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.meters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[Meter], meter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.archive(
            "id",
        )
        assert meter is None

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.meters.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert meter is None

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.meters.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert meter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meters.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncDodoPayments) -> None:
        meter = await async_client.meters.unarchive(
            "id",
        )
        assert meter is None

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.meters.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meter = await response.parse()
        assert meter is None

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.meters.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meter = await response.parse()
            assert meter is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meters.with_raw_response.unarchive(
                "",
            )
