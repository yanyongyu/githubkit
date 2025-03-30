from collections.abc import Awaitable
from typing import Any, Callable, Generic, Optional, TypeVar, Union, cast, overload
from typing_extensions import ParamSpec, Self, deprecated

from .response import Response
from .utils import is_async

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")
RTS = TypeVar("RTS")

R = Union[
    Callable[CP, Response[RT]],
    Callable[CP, Awaitable[Response[RT]]],
]


@deprecated(
    "Legacy pagination based on page and per_page is deprecated. "
    "Use github.rest.paginate instead."
)
class Paginator(Generic[RT]):
    """Paginate through the responses of the rest api request."""

    @overload
    def __init__(
        self: "Paginator[RTS]",
        request: R[CP, list[RTS]],
        page: int = 1,
        per_page: int = 100,
        map_func: None = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ): ...

    @overload
    def __init__(
        self: "Paginator[RTS]",
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Callable[[Response[CT]], list[RTS]] = ...,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ): ...

    def __init__(
        self,
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Optional[Callable[[Response[CT]], list[RT]]] = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ):
        self.request = request
        self.args = args
        self.kwargs = kwargs

        self.map_func = map_func

        self._current_page: int = page
        self._per_page: int = per_page

        self._index: int = 0
        self._cached_data: list[RT] = []

    def __next__(self) -> RT:
        if self._index >= len(self._cached_data):
            contents = self._get_next_page()
            if not contents:
                raise StopIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __iter__(self: Self) -> Self:
        if is_async(self.request):
            raise TypeError(f"Request method {self.request} is not an sync function")
        return self

    async def __anext__(self) -> RT:
        if self._index >= len(self._cached_data):
            contents = await self._aget_next_page()
            if not contents:
                raise StopAsyncIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __aiter__(self: Self) -> Self:
        if not is_async(self.request):
            raise TypeError(f"Request method {self.request} is not an async function")
        return self

    def _get_next_page(self) -> list[RT]:
        response = cast(
            Response[Any],
            self.request(
                *self.args,
                **self.kwargs,
                page=self._current_page,  # type: ignore
                per_page=self._per_page,  # type: ignore
            ),
        )
        self._cached_data = (
            cast(Response[list[RT]], response).parsed_data
            if self.map_func is None
            else self.map_func(response)
        )
        self._index = 0
        self._current_page += 1
        return self._cached_data

    async def _aget_next_page(self) -> list[RT]:
        response = cast(
            Response[Any],
            await self.request(
                *self.args,
                **self.kwargs,
                page=self._current_page,  # type: ignore
                per_page=self._per_page,  # type: ignore
            ),
        )
        self._cached_data = (
            cast(Response[list[RT]], response).parsed_data
            if self.map_func is None
            else self.map_func(response)
        )
        self._index = 0
        self._current_page += 1
        return self._cached_data
