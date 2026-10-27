from __future__ import annotations

import os
import time
import asyncio
import inspect
import threading
from typing import Dict, Union, Callable, Optional, Awaitable
from dataclasses import dataclass
from typing_extensions import override

import httpx

from ._utils import is_dict, asyncify, parse_datetime
from ._exceptions import DodoPaymentsError

__all__ = [
    "WorkloadIdentity",
    "SubjectTokenContext",
    "SubjectTokenProvider",
    "SubjectTokenFunction",
    "SubjectTokenSource",
    "github_actions",
    "gitlab",
    "terraform_cloud",
    "gcp",
    "vercel",
    "kubernetes",
    "file",
    "aws",
    "static",
    "auto",
]

IDENTITY_PROVIDER_ID_ENV = "DODO_PAYMENTS_IDENTITY_PROVIDER_ID"
IDENTITY_TOKEN_FILE_ENV = "DODO_PAYMENTS_IDENTITY_TOKEN_FILE"
KUBERNETES_TOKEN_PATH = "/var/run/secrets/tokens/dodo-token"
GCP_IDENTITY_URL = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"

# The client gets a new access token when 300 seconds or less remain.
REFRESH_WINDOW_SECONDS = 300.0

_HELPER_TIMEOUT = httpx.Timeout(10.0)


@dataclass(frozen=True)
class SubjectTokenContext:
    """The data that the client gives to a subject token provider."""

    base_url: str
    """The base URL of the client."""

    audience: str
    """The origin of the client base URL, for example `https://live.dodopayments.com`."""


class SubjectTokenProvider:
    """A source of subject tokens (JWTs) for the workload identity token exchange.

    Override `get_token`. Override `aget_token` too if the source must not block the event loop.
    """

    def get_token(self, context: SubjectTokenContext) -> str:
        raise NotImplementedError()

    async def aget_token(self, context: SubjectTokenContext) -> str:
        return await asyncify(self.get_token)(context)


SubjectTokenFunction = Callable[[], Union[str, Awaitable[str]]]
"""A function that returns a subject token (JWT). The function can be async."""

SubjectTokenSource = Union[SubjectTokenProvider, SubjectTokenFunction]


def _checked(token: str, source: str) -> str:
    token = token.strip()
    if not token:
        raise DodoPaymentsError(f"The {source} subject token source returned an empty token")
    return token


class _FunctionProvider(SubjectTokenProvider):
    def __init__(self, function: SubjectTokenFunction) -> None:
        self._function = function

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        result = self._function()
        if isinstance(result, str):
            return _checked(result, "function")
        if inspect.iscoroutine(result):
            result.close()
        raise DodoPaymentsError("The subject token function is async. Use the async client with an async function.")

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        result = self._function()
        if not isinstance(result, str):
            result = await result
        return _checked(result, "function")


class _StaticProvider(SubjectTokenProvider):
    def __init__(self, token: str) -> None:
        self._token = _checked(token, "static")

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        return self._token

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        return self._token


class _EnvProvider(SubjectTokenProvider):
    def __init__(self, *names: str) -> None:
        self._names = names

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        for name in self._names:
            value = os.environ.get(name)
            if value and value.strip():
                return value.strip()
        raise DodoPaymentsError(f"The {' or '.join(self._names)} environment variable is not set")

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        return self.get_token(context)


class _FileProvider(SubjectTokenProvider):
    def __init__(self, path: Union[str, os.PathLike[str], None]) -> None:
        self._path = path

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        path = self._path if self._path is not None else os.environ.get(IDENTITY_TOKEN_FILE_ENV)
        if not path:
            raise DodoPaymentsError(
                f"Give a path to the file subject token source or set the {IDENTITY_TOKEN_FILE_ENV} environment variable"
            )
        with open(path, encoding="utf-8") as token_file:
            return _checked(token_file.read(), "file")


def _origin(base_url: Union[str, httpx.URL]) -> str:
    url = httpx.URL(str(base_url))
    return f"{url.scheme}://{url.netloc.decode('ascii')}"


class _GitHubActionsProvider(SubjectTokenProvider):
    def __init__(self, audience: Optional[str]) -> None:
        self._audience = audience

    def _request(self, context: SubjectTokenContext) -> httpx.Request:
        request_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
        request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
        if not request_url or not request_token:
            raise DodoPaymentsError(
                "The ACTIONS_ID_TOKEN_REQUEST_URL and ACTIONS_ID_TOKEN_REQUEST_TOKEN environment variables are not set. "
                "Give the job the `id-token: write` permission."
            )
        url = httpx.URL(request_url).copy_merge_params({"audience": self._audience or context.audience})
        return httpx.Request(
            "GET", url, headers={"Authorization": f"bearer {request_token}", "Accept": "application/json"}
        )

    @staticmethod
    def _parse(response: httpx.Response) -> str:
        if response.status_code != 200:
            raise DodoPaymentsError(f"The GitHub Actions OIDC token request failed with status {response.status_code}")
        data: object = response.json()
        value = data.get("value") if is_dict(data) else None
        if not isinstance(value, str):
            raise DodoPaymentsError("The GitHub Actions OIDC token response has no `value` field")
        return _checked(value, "github_actions")

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        with httpx.Client(timeout=_HELPER_TIMEOUT) as client:
            return self._parse(client.send(self._request(context)))

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        async with httpx.AsyncClient(timeout=_HELPER_TIMEOUT) as client:
            return self._parse(await client.send(self._request(context)))


class _GCPProvider(SubjectTokenProvider):
    def __init__(self, audience: Optional[str]) -> None:
        self._audience = audience

    def _request(self, context: SubjectTokenContext) -> httpx.Request:
        return httpx.Request(
            "GET",
            GCP_IDENTITY_URL,
            params={"audience": self._audience or context.audience, "format": "full"},
            headers={"Metadata-Flavor": "Google"},
        )

    @staticmethod
    def _parse(response: httpx.Response) -> str:
        if response.status_code != 200:
            raise DodoPaymentsError(
                f"The GCP metadata identity token request failed with status {response.status_code}"
            )
        return _checked(response.text, "gcp")

    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        with httpx.Client(timeout=_HELPER_TIMEOUT) as client:
            return self._parse(client.send(self._request(context)))

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        async with httpx.AsyncClient(timeout=_HELPER_TIMEOUT) as client:
            return self._parse(await client.send(self._request(context)))


def github_actions(audience: Optional[str] = None) -> SubjectTokenProvider:
    """Get a new GitHub Actions OIDC token for each exchange.

    The default audience is the origin of the client base URL. The job must have the `id-token: write` permission.
    """
    return _GitHubActionsProvider(audience)


def gitlab(env_var: str = "DODO_PAYMENTS_ID_TOKEN") -> SubjectTokenProvider:
    """Read a GitLab CI/CD ID token from an environment variable (see `id_tokens` in `.gitlab-ci.yml`)."""
    return _EnvProvider(env_var)


def terraform_cloud() -> SubjectTokenProvider:
    """Read the HCP Terraform workload identity token from `TFC_WORKLOAD_IDENTITY_TOKEN`."""
    return _EnvProvider("TFC_WORKLOAD_IDENTITY_TOKEN", "TFC_WORKLOAD_IDENTITY_TOKEN_DODO")


def gcp(audience: Optional[str] = None) -> SubjectTokenProvider:
    """Get a Google-signed identity token from the GCP metadata server for each exchange."""
    return _GCPProvider(audience)


def vercel() -> SubjectTokenProvider:
    """Read the Vercel OIDC token from `VERCEL_OIDC_TOKEN`."""
    return _EnvProvider("VERCEL_OIDC_TOKEN")


def kubernetes(path: Union[str, os.PathLike[str]] = KUBERNETES_TOKEN_PATH) -> SubjectTokenProvider:
    """Read a projected Kubernetes service account token from a file for each exchange."""
    return _FileProvider(path)


def file(path: Union[str, os.PathLike[str], None] = None) -> SubjectTokenProvider:
    """Read a token from a file for each exchange. The default path is the value of `DODO_PAYMENTS_IDENTITY_TOKEN_FILE`."""
    return _FileProvider(path)


def aws(function: SubjectTokenFunction) -> SubjectTokenProvider:
    """Use a function that returns an AWS-issued JWT, for example from STS `GetWebIdentityToken`."""
    return _FunctionProvider(function)


def static(token: str) -> SubjectTokenProvider:
    """Use the same token for each exchange. Use this for tests."""
    return _StaticProvider(token)


def _detect() -> Optional[SubjectTokenProvider]:
    if os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL") and os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN"):
        return github_actions()
    if os.environ.get("TFC_WORKLOAD_IDENTITY_TOKEN") or os.environ.get("TFC_WORKLOAD_IDENTITY_TOKEN_DODO"):
        return terraform_cloud()
    if os.environ.get(IDENTITY_TOKEN_FILE_ENV):
        return file()
    if os.path.isfile(KUBERNETES_TOKEN_PATH):
        return kubernetes()
    return None


def auto() -> SubjectTokenProvider:
    """Find the subject token source of the current environment.

    The order is: GitHub Actions, HCP Terraform, `DODO_PAYMENTS_IDENTITY_TOKEN_FILE`, the Kubernetes default token path.
    """
    provider = _detect()
    if provider is None:
        raise DodoPaymentsError(
            "No workload identity subject token source was found. Give a provider to `WorkloadIdentity`."
        )
    return provider


class _TokenCache:
    def __init__(self) -> None:
        self.access_token: Optional[str] = None
        self._refresh_at = 0.0
        self.sync_lock = threading.Lock()
        self._async_lock: Optional[asyncio.Lock] = None
        self._async_lock_loop: Optional[asyncio.AbstractEventLoop] = None

    def valid_token(self) -> Optional[str]:
        token = self.access_token
        if token is not None and time.time() < self._refresh_at:
            return token
        return None

    def async_lock(self) -> asyncio.Lock:
        loop = asyncio.get_running_loop()
        if self._async_lock is None or self._async_lock_loop is not loop:
            self._async_lock = asyncio.Lock()
            self._async_lock_loop = loop
        return self._async_lock

    def store(self, data: object) -> str:
        if not is_dict(data):
            raise DodoPaymentsError("The workload identity token response is not a JSON object")
        access_token = data.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            raise DodoPaymentsError("The workload identity token response has no `access_token` field")
        expires_at = data.get("expires_at")
        expires_in = data.get("expires_in")
        expiry: Optional[float] = None
        if isinstance(expires_at, str):
            try:
                expiry = parse_datetime(expires_at).timestamp()
            except (TypeError, ValueError):
                expiry = None
        if expiry is None and isinstance(expires_in, (int, float)) and not isinstance(expires_in, bool):
            expiry = time.time() + float(expires_in)
        self.access_token = access_token
        self._refresh_at = (time.time() if expiry is None else expiry) - REFRESH_WINDOW_SECONDS
        return access_token

    def invalidate(self, token: Optional[str]) -> None:
        if token is not None and self.access_token == token:
            self.access_token = None
            self._refresh_at = 0.0


class WorkloadIdentity:
    """The `workload_identity` client option.

    The client exchanges a subject token (a JWT from your workload platform) for a short-lived access token.
    Clients that share this object also share the cached access token.
    """

    identity_provider_id: str
    provider: SubjectTokenProvider

    def __init__(
        self,
        *,
        identity_provider_id: Optional[str] = None,
        provider: Optional[SubjectTokenSource] = None,
    ) -> None:
        """
        Args:
          identity_provider_id: The `wip_...` ID. The default is the value of `DODO_PAYMENTS_IDENTITY_PROVIDER_ID`.

          provider: The subject token source. The default is `auto()`.
        """
        if identity_provider_id is None:
            identity_provider_id = os.environ.get(IDENTITY_PROVIDER_ID_ENV)
        if not identity_provider_id:
            raise DodoPaymentsError(
                f"The identity_provider_id workload identity option must be set either by passing identity_provider_id or by setting the {IDENTITY_PROVIDER_ID_ENV} environment variable"
            )
        self.identity_provider_id = identity_provider_id
        if provider is None:
            self.provider = auto()
        elif isinstance(provider, SubjectTokenProvider):
            self.provider = provider
        else:
            self.provider = _FunctionProvider(provider)
        self._caches: Dict[str, _TokenCache] = {}
        self._caches_lock = threading.Lock()

    @classmethod
    def from_env(cls) -> Optional[WorkloadIdentity]:
        """Return the configuration from the environment, or `None` if the environment does not configure it."""
        identity_provider_id = os.environ.get(IDENTITY_PROVIDER_ID_ENV)
        if not identity_provider_id:
            return None
        provider = _detect()
        if provider is None:
            return None
        return cls(identity_provider_id=identity_provider_id, provider=provider)

    def _cache_for(self, base_url: Union[str, httpx.URL]) -> _TokenCache:
        key = str(base_url)
        with self._caches_lock:
            cache = self._caches.get(key)
            if cache is None:
                cache = self._caches[key] = _TokenCache()
            return cache

    def _context(self, base_url: Union[str, httpx.URL]) -> SubjectTokenContext:
        return SubjectTokenContext(base_url=str(base_url), audience=_origin(base_url))

    @override
    def __repr__(self) -> str:
        return f"WorkloadIdentity(identity_provider_id={self.identity_provider_id!r}, provider={self.provider!r})"
