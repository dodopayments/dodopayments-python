from __future__ import annotations

from typing import Dict, Type, Union, Optional, overload
from typing_extensions import Literal, override

import httpx

from ._types import Omit, Headers, ResponseT
from ._utils import is_given
from ._compat import cached_property
from ._models import FinalRequestOptions
from ._exceptions import APITimeoutError, APIConnectionError, AuthenticationError
from ._base_client import SyncAPIClient, AsyncAPIClient, _StreamT, _AsyncStreamT
from .workload_identity import WorkloadIdentity

__all__ = [
    "SyncWorkloadIdentityAPIClient",
    "AsyncWorkloadIdentityAPIClient",
    "WorkloadIdentityResource",
    "AsyncWorkloadIdentityResource",
]

TOKEN_PATH = "/workload-identity/token"
REVOKE_PATH = "/workload-identity/token/revoke"

_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:token-exchange"
_SUBJECT_TOKEN_TYPE = "urn:ietf:params:oauth:token-type:jwt"


def _exchange_body(config: WorkloadIdentity, subject_token: str) -> Dict[str, str]:
    return {
        "grant_type": _GRANT_TYPE,
        "subject_token_type": _SUBJECT_TOKEN_TYPE,
        "subject_token": subject_token,
        "identity_provider_id": config.identity_provider_id,
    }


def _has_authorization(headers: Union[Headers, None]) -> bool:
    return any(name.lower() == "authorization" for name in headers or {})


def _used_token(response: httpx.Response) -> Optional[str]:
    scheme, _, token = response.request.headers.get("Authorization", "").partition(" ")
    return token if scheme.lower() == "bearer" and token else None


# The token exchange and the revoke request do not go through `request()`: the debug log of the
# request options must not show the subject token or the access token.
def _build_direct_request(
    client: Union[SyncAPIClient, AsyncAPIClient], path: str, *, body: Optional[Dict[str, str]], token: Optional[str]
) -> httpx.Request:
    headers = {
        name: value
        for name, value in client.default_headers.items()
        if not isinstance(value, Omit) and name.lower() != "authorization"
    }
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    return httpx.Request(
        "POST",
        client._prepare_url(path),
        json=body,
        headers=headers,
        extensions={"timeout": httpx.Timeout(client.timeout).as_dict()},
    )


class SyncWorkloadIdentityAPIClient(SyncAPIClient):
    _workload_identity: Optional[WorkloadIdentity]

    @cached_property
    def workload_identity(self) -> WorkloadIdentityResource:
        """Manage the workload identity access token of this client."""
        return WorkloadIdentityResource(self)

    def _workload_identity_send(
        self, path: str, *, body: Optional[Dict[str, str]] = None, token: Optional[str] = None
    ) -> httpx.Response:
        options = FinalRequestOptions.construct(method="post", url=path)
        for retries_taken in range(self.max_retries + 1):
            remaining_retries = self.max_retries - retries_taken
            request = _build_direct_request(self, path, body=body, token=token)
            try:
                response = self._client.send(request)
            except Exception as err:
                if remaining_retries > 0:
                    self._sleep_for_retry(
                        retries_taken=retries_taken, max_retries=self.max_retries, options=options, response=None
                    )
                    continue
                if isinstance(err, httpx.TimeoutException):
                    raise APITimeoutError(request=request) from err
                raise APIConnectionError(request=request) from err
            if response.is_success:
                response.read()
                return response
            if remaining_retries > 0 and self._should_retry(response):
                response.close()
                self._sleep_for_retry(
                    retries_taken=retries_taken, max_retries=self.max_retries, options=options, response=response
                )
                continue
            response.read()
            raise self._make_status_error_from_response(response)
        raise RuntimeError("unreachable")

    def _workload_identity_token(self, config: WorkloadIdentity) -> str:
        cache = config._cache_for(self.base_url)
        token = cache.valid_token()
        if token is not None:
            return token
        with cache.sync_lock:
            token = cache.valid_token()
            if token is None:
                subject_token = config.provider.get_token(config._context(self.base_url))
                response = self._workload_identity_send(TOKEN_PATH, body=_exchange_body(config, subject_token))
                token = cache.store(response.json())
            return token

    @override
    def _prepare_request(self, request: httpx.Request) -> None:
        super()._prepare_request(request)
        config = self._workload_identity
        if config is not None and "Authorization" not in request.headers:
            request.headers["Authorization"] = f"Bearer {self._workload_identity_token(config)}"

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        if (
            self._workload_identity is not None
            and response.status_code < 500
            and response.request.url.path.endswith(TOKEN_PATH)
        ):
            return False
        return super()._should_retry(response)

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[True],
        stream_cls: Type[_StreamT],
    ) -> _StreamT: ...

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: Union[Type[_StreamT], None] = None,
    ) -> Union[ResponseT, _StreamT]: ...

    @override
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: Union[Type[_StreamT], None] = None,
    ) -> Union[ResponseT, _StreamT]:
        try:
            return super().request(cast_to, options, stream=stream, stream_cls=stream_cls)
        except AuthenticationError as err:
            config = self._workload_identity
            if (
                config is None
                or _has_authorization(self._custom_headers)
                or _has_authorization(options.headers if is_given(options.headers) else None)
            ):
                raise
            # One new exchange and one retry. A second 401 goes to the caller.
            config._cache_for(self.base_url).invalidate(_used_token(err.response))
            return super().request(cast_to, options, stream=stream, stream_cls=stream_cls)


class AsyncWorkloadIdentityAPIClient(AsyncAPIClient):
    _workload_identity: Optional[WorkloadIdentity]

    @cached_property
    def workload_identity(self) -> AsyncWorkloadIdentityResource:
        """Manage the workload identity access token of this client."""
        return AsyncWorkloadIdentityResource(self)

    async def _workload_identity_send(
        self, path: str, *, body: Optional[Dict[str, str]] = None, token: Optional[str] = None
    ) -> httpx.Response:
        options = FinalRequestOptions.construct(method="post", url=path)
        for retries_taken in range(self.max_retries + 1):
            remaining_retries = self.max_retries - retries_taken
            request = _build_direct_request(self, path, body=body, token=token)
            try:
                response = await self._client.send(request)
            except Exception as err:
                if remaining_retries > 0:
                    await self._sleep_for_retry(
                        retries_taken=retries_taken, max_retries=self.max_retries, options=options, response=None
                    )
                    continue
                if isinstance(err, httpx.TimeoutException):
                    raise APITimeoutError(request=request) from err
                raise APIConnectionError(request=request) from err
            if response.is_success:
                await response.aread()
                return response
            if remaining_retries > 0 and self._should_retry(response):
                await response.aclose()
                await self._sleep_for_retry(
                    retries_taken=retries_taken, max_retries=self.max_retries, options=options, response=response
                )
                continue
            await response.aread()
            raise self._make_status_error_from_response(response)
        raise RuntimeError("unreachable")

    async def _workload_identity_token(self, config: WorkloadIdentity) -> str:
        cache = config._cache_for(self.base_url)
        token = cache.valid_token()
        if token is not None:
            return token
        async with cache.async_lock():
            token = cache.valid_token()
            if token is None:
                subject_token = await config.provider.aget_token(config._context(self.base_url))
                response = await self._workload_identity_send(TOKEN_PATH, body=_exchange_body(config, subject_token))
                token = cache.store(response.json())
            return token

    @override
    async def _prepare_request(self, request: httpx.Request) -> None:
        await super()._prepare_request(request)
        config = self._workload_identity
        if config is not None and "Authorization" not in request.headers:
            request.headers["Authorization"] = f"Bearer {await self._workload_identity_token(config)}"

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        if (
            self._workload_identity is not None
            and response.status_code < 500
            and response.request.url.path.endswith(TOKEN_PATH)
        ):
            return False
        return super()._should_retry(response)

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[True],
        stream_cls: Type[_AsyncStreamT],
    ) -> _AsyncStreamT: ...

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool,
        stream_cls: Union[Type[_AsyncStreamT], None] = None,
    ) -> Union[ResponseT, _AsyncStreamT]: ...

    @override
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: Union[Type[_AsyncStreamT], None] = None,
    ) -> Union[ResponseT, _AsyncStreamT]:
        try:
            return await super().request(cast_to, options, stream=stream, stream_cls=stream_cls)
        except AuthenticationError as err:
            config = self._workload_identity
            if (
                config is None
                or _has_authorization(self._custom_headers)
                or _has_authorization(options.headers if is_given(options.headers) else None)
            ):
                raise
            # One new exchange and one retry. A second 401 goes to the caller.
            config._cache_for(self.base_url).invalidate(_used_token(err.response))
            return await super().request(cast_to, options, stream=stream, stream_cls=stream_cls)


class WorkloadIdentityResource:
    """The workload identity operations of a client."""

    def __init__(self, client: SyncWorkloadIdentityAPIClient) -> None:
        self._client = client

    def revoke(self) -> None:
        """Revoke the cached access token and clear the cache. If no token is cached, this method does nothing."""
        config = self._client._workload_identity
        if config is None:
            return
        cache = config._cache_for(self._client.base_url)
        token = cache.access_token
        if token is None:
            return
        try:
            self._client._workload_identity_send(REVOKE_PATH, token=token)
        finally:
            cache.invalidate(token)


class AsyncWorkloadIdentityResource:
    """The workload identity operations of a client."""

    def __init__(self, client: AsyncWorkloadIdentityAPIClient) -> None:
        self._client = client

    async def revoke(self) -> None:
        """Revoke the cached access token and clear the cache. If no token is cached, this method does nothing."""
        config = self._client._workload_identity
        if config is None:
            return
        cache = config._cache_for(self._client.base_url)
        token = cache.access_token
        if token is None:
            return
        try:
            await self._client._workload_identity_send(REVOKE_PATH, token=token)
        finally:
            cache.invalidate(token)
