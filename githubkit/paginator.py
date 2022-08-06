import inspect
from typing_extensions import Self, ParamSpec
from typing import (
    List,
    Union,
    Generic,
    TypeVar,
    Callable,
    Optional,
    Awaitable,
    cast,
    overload,
)

from .utils import is_async
from .response import Response

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")

R = Union[
    Callable[CP, Response[List[RT]]],
    Callable[CP, Awaitable[Response[List[RT]]]],
]


class Paginator(Generic[RT]):
    @overload
    def __init__(
        self: "Paginator[RT]",
        request: R[CP, RT],
        page: int = 1,
        per_page: int = 100,
        map_func: None = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ):
        ...

    @overload
    def __init__(
        self: "Paginator[RT]",
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Callable[[Response[List[CT]]], List[RT]] = ...,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ):
        ...

    def __init__(
        self,
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Optional[Callable[[Response[List[CT]]], List[RT]]] = None,
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
        self._cached_data: List[RT] = []

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

    def _get_next_page(self) -> List[RT]:
        response = self.request(
            *self.args,
            **self.kwargs,
            page=self._current_page,  # type: ignore
            per_page=self._per_page,  # type: ignore
        )
        self._cached_data = (
            cast(Response[List[RT]], response).parsed_data
            if self.map_func is None
            else self.map_func(response)
        )
        self._index = 0
        self._current_page += 1
        return self._cached_data

    async def _aget_next_page(self) -> List[RT]:
        response = await self.request(
            *self.args,
            **self.kwargs,
            page=self._current_page,  # type: ignore
            per_page=self._per_page,  # type: ignore
        )
        self._cached_data = (
            cast(Response[List[RT]], response).parsed_data
            if self.map_func is None
            else self.map_func(response)
        )
        self._index = 0
        self._current_page += 1
        return self._cached_data
