import inspect
from typing_extensions import Self, ParamSpec
from typing import List, Union, Generic, TypeVar, Callable, Awaitable

from .response import Response

RT = TypeVar("RT")
CP = ParamSpec("CP")


class Paginator(Generic[RT]):
    def __init__(
        self,
        request: Union[
            Callable[CP, Response[List[RT]]],
            Callable[CP, Awaitable[Response[List[RT]]]],
        ],
        page: int = 1,
        per_page: int = 100,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ):
        self.request = request
        self.args = args
        self.kwargs = kwargs

        self._current_page: int = page
        self._per_page: int = per_page

        self._index: int = 0
        self._cached_data: List[RT] = []

    @property
    def _is_async(self):
        return inspect.isroutine(self.request) and inspect.iscoroutinefunction(
            self.request
        )

    def __next__(self) -> RT:
        if self._index >= len(self._cached_data):
            contents = self._get_next_page()
            if not contents:
                raise StopIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __iter__(self: Self) -> Self:
        if self._is_async:
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
        if not self._is_async:
            raise TypeError(f"Request method {self.request} is not an async function")
        return self

    def _get_next_page(self) -> List[RT]:
        response: Response[List[RT]] = self.request(
            *self.args,
            **self.kwargs,
            page=self._current_page,  # type: ignore
            per_page=self._per_page,  # type: ignore
        )
        self._cached_data = response.parsed_data
        self._index = 0
        self._current_page += 1
        return self._cached_data

    async def _aget_next_page(self) -> List[RT]:
        response: Response[List[RT]] = await self.request(
            *self.args,
            **self.kwargs,
            page=self._current_page,  # type: ignore
            per_page=self._per_page,  # type: ignore
        )
        self._cached_data = response.parsed_data
        self._index = 0
        self._current_page += 1
        return self._cached_data
