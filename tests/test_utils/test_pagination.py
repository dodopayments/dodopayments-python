from dodopayments.pagination import SyncCursorPagePagination, AsyncCursorPagePagination


def test_sync_cursor_pagination_respects_done_flag() -> None:
    page = SyncCursorPagePagination.construct(
        data=[{"id": "wh_1"}],
        iterator="cursor-abc",
        done=True,
    )
    assert page.has_next_page() is False


def test_async_cursor_pagination_respects_done_flag() -> None:
    page = AsyncCursorPagePagination.construct(
        data=[{"id": "wh_1"}],
        iterator="cursor-abc",
        done=True,
    )
    assert page.has_next_page() is False