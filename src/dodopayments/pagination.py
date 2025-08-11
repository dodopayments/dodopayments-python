# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncDefaultPageNumberPagination",
    "AsyncDefaultPageNumberPagination",
    "SyncCursorPagePagination",
    "AsyncCursorPagePagination",
]

_T = TypeVar("_T")


class SyncDefaultPageNumberPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page_number")) or 1

        return PageInfo(params={"page_number": last_page + 1})


class AsyncDefaultPageNumberPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page_number")) or 1

        return PageInfo(params={"page_number": last_page + 1})


class SyncCursorPagePagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    iterator: Optional[str] = None
    done: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        done = self.done
        if done is not None and done is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        iterator = self.iterator
        if not iterator:
            return None

        return PageInfo(params={"iterator": iterator})


class AsyncCursorPagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    iterator: Optional[str] = None
    done: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        done = self.done
        if done is not None and done is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        iterator = self.iterator
        if not iterator:
            return None

        return PageInfo(params={"iterator": iterator})
