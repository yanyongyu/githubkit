from collections.abc import Awaitable
import re
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Optional,
    TypeVar,
    Union,
    cast,
    overload,
)
from typing_extensions import ParamSpec, Self

import httpx

from githubkit.response import Response
from githubkit.utils import is_async

if TYPE_CHECKING:
    from githubkit.versions import RestVersionSwitcher

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")
RTS = TypeVar("RTS")

R = Union[
    Callable[CP, Response[RT]],
    Callable[CP, Awaitable[Response[RT]]],
]

# https://github.com/octokit/plugin-paginate-rest.js/blob/1f44b5469b31ddec9621000e6e1aee63c71ea8bf/src/iterator.ts#L40
NEXT_LINK_PATTERN = r'<([^<>]+)>;\s*rel="next"'


# https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api
# https://github.com/octokit/plugin-paginate-rest.js/blob/1f44b5469b31ddec9621000e6e1aee63c71ea8bf/src/iterator.ts
class Paginator(Generic[RT]):
    """Paginate through the responses of the rest api request."""

    @overload
    def __init__(
        self: "Paginator[RTS]",
        rest: "RestVersionSwitcher",
        request: R[CP, list[RTS]],
        map_func: None = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ): ...

    @overload
    def __init__(
        self: "Paginator[RTS]",
        rest: "RestVersionSwitcher",
        request: R[CP, CT],
        map_func: Callable[[Response[CT]], list[RTS]],
        *args: CP.args,
        **kwargs: CP.kwargs,
    ): ...

    def __init__(
        self,
        rest: "RestVersionSwitcher",
        request: R[CP, CT],
        map_func: Optional[Callable[[Response[CT]], list[RT]]] = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ):
        self.rest = rest

        self.request = request
        self.args = args
        self.kwargs = kwargs

        self.map_func = map_func

        self._initialized: bool = False
        self._request_method: Optional[str] = None
        self._response_model: Optional[Any] = None
        self._next_link: Optional[httpx.URL] = None

        self._index: int = 0
        self._cached_data: list[RT] = []

    @property
    def finalized(self) -> bool:
        """Whether the paginator is finalized or not."""
        return self._initialized and self._next_link is None

    def reset(self) -> None:
        """Reset the paginator to the initial state."""

        self._initialized = False
        self._next_link = None
        self._index = 0
        self._cached_data = []

    def __next__(self) -> RT:
        while self._index >= len(self._cached_data):
            self._get_next_page()
            if self.finalized:
                raise StopIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __iter__(self: Self) -> Self:
        if is_async(self.request):
            raise TypeError(f"Request method {self.request} is not an sync function")
        return self

    async def __anext__(self) -> RT:
        while self._index >= len(self._cached_data):
            await self._aget_next_page()
            if self.finalized:
                raise StopAsyncIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __aiter__(self: Self) -> Self:
        if not is_async(self.request):
            raise TypeError(f"Request method {self.request} is not an async function")
        return self

    def _find_next_link(self, response: Response[Any]) -> Optional[httpx.URL]:
        """Find the next link in the response headers."""
        if links := response.headers.get("link"):
            if match := re.search(NEXT_LINK_PATTERN, links):
                return httpx.URL(match.group(1))
        return None

    def _apply_map_func(self, response: Response[Any]) -> list[RT]:
        if self.map_func is not None:
            result = self.map_func(response)
            if not isinstance(result, list):
                raise TypeError(f"Map function must return a list, got {type(result)}")
        else:
            result = cast(Response[list[RT]], response).parsed_data
            if not isinstance(result, list):
                raise TypeError(f"Response is not a list, got {type(result)}")
        return result

    def _fill_cache_data(self, data: list[RT]) -> None:
        """Fill the cache with the data."""
        self._cached_data = data
        self._index = 0

    def _get_next_page(self) -> None:
        if not self._initialized:
            # First request
            response = cast(
                Response[Any],
                self.request(*self.args, **self.kwargs),
            )
            self._initialized = True
            self._request_method = response.raw_request.method
        else:
            # Next request
            if self._next_link is None:
                raise RuntimeError("Paginator is finalized, no more pages to fetch.")
            if self._request_method is None:
                raise RuntimeError("Request method is not set, this should not happen.")
            if self._response_model is None:
                raise RuntimeError("Response model is not set, this should not happen.")

            # we request the next page with the same method and response model
            response = cast(
                Response[Any],
                self.rest._github.request(
                    self._request_method,
                    self._next_link,
                    headers=self.kwargs.get("headers"),  # type: ignore
                    response_model=self._response_model,  # type: ignore
                ),
            )

        self._next_link = self._find_next_link(response)
        self._fill_cache_data(self._apply_map_func(response))

    async def _aget_next_page(self) -> None:
        if not self._initialized:
            # First request
            response = cast(
                Response[Any],
                await self.request(*self.args, **self.kwargs),  # type: ignore
            )
            self._initialized = True
            self._request_method = response.raw_request.method
        else:
            # Next request
            if self._next_link is None:
                raise RuntimeError("Paginator is finalized, no more pages to fetch.")
            if self._request_method is None:
                raise RuntimeError("Request method is not set, this should not happen.")
            if self._response_model is None:
                raise RuntimeError("Response model is not set, this should not happen.")

            response = cast(
                Response[Any],
                await self.rest._github.request(
                    self._request_method,
                    self._next_link,
                    headers=self.kwargs.get("headers"),  # type: ignore
                    response_model=self._response_model,  # type: ignore
                ),
            )

        self._next_link = self._find_next_link(response)
        self._fill_cache_data(self._apply_map_func(response))
