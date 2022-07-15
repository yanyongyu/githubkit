from typing_extensions import Self, ParamSpec
from typing import List, Generic, TypeVar, Callable, Awaitable

from .response import Response

RT = TypeVar("RT")
CP = ParamSpec("CP")


class Paginator(Generic[RT]):
    def __init__(
        self,
        request: Callable[CP, Awaitable[Response[List[RT]]]],
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

    async def __anext__(self) -> RT:
        if self._index >= len(self._cached_data):
            contents = await self._get_next_page()
            if not contents:
                raise StopAsyncIteration

        current = self._cached_data[self._index]
        self._index += 1
        return current

    def __aiter__(self: Self) -> Self:
        return self

    async def _get_next_page(self) -> List[RT]:
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


def paginate(
    request: Callable[CP, Awaitable[Response[List[RT]]]],
    page: int = 1,
    per_page: int = 100,
    *args: CP.args,
    **kwargs: CP.kwargs,
) -> Paginator[RT]:
    return Paginator(request, page, per_page, *args, **kwargs)
