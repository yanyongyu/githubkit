from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Optional, TypedDict
from typing_extensions import Self
from weakref import ref

from githubkit.exception import GraphQLMissingCursorChange, GraphQLMissingPageInfo

if TYPE_CHECKING:
    from githubkit.response import Response

    from . import GraphQLNamespace
    from .models import GraphQLResponse

CURSOR_VARNAME = "cursor"


class PageInfo(TypedDict, total=False):
    """PageInfo object returned by the GraphQL API.

    See: https://docs.github.com/en/graphql/reference/objects#pageinfo
    """

    hasNextPage: bool
    hasPreviousPage: bool
    startCursor: str
    endCursor: str


class Paginator:
    def __init__(
        self,
        graphql: "GraphQLNamespace",
        query: str,
        variables: Optional[Mapping[str, Any]] = None,
    ) -> None:
        self._graphql_ref = ref(graphql)
        self.query = query

        self._has_next_page: bool = True
        self._current_variables = dict(variables) if variables is not None else {}

    @property
    def _graphql(self) -> "GraphQLNamespace":
        if g := self._graphql_ref():
            return g
        raise RuntimeError(
            "GraphQL client has already been collected. "
            "Do not use the paginator after the client has been collected."
        )

    def __next__(self) -> dict[str, Any]:
        if not self._has_next_page:
            raise StopIteration

        return self._get_next_page()

    def __iter__(self: Self) -> Self:
        return self

    async def __anext__(self) -> dict[str, Any]:
        if not self._has_next_page:
            raise StopAsyncIteration

        return await self._aget_next_page()

    def __aiter__(self: Self) -> Self:
        return self

    def _extract_page_info(self, data: dict[str, Any]) -> Optional[PageInfo]:
        if "pageInfo" in data:
            return data["pageInfo"]

        for value in data.values():
            if isinstance(value, dict):
                return self._extract_page_info(value)

        # not found
        return None

    def _extract_has_next_page(self, page_info: PageInfo) -> bool:
        return (
            page_info["hasNextPage"]
            if "hasNextPage" in page_info
            else page_info["hasPreviousPage"]  # type: ignore
        )

    def _extract_cursor(self, page_info: PageInfo) -> str:
        return (
            page_info["endCursor"]  # type: ignore
            if "hasNextPage" in page_info
            else page_info["startCursor"]  # type: ignore
        )

    def _do_update(self, response: "Response[GraphQLResponse]") -> dict[str, Any]:
        result = self._graphql.parse_graphql_response(response)

        page_info = self._extract_page_info(result)
        if page_info is None:
            raise GraphQLMissingPageInfo(response.parsed_data)

        self._has_next_page = self._extract_has_next_page(page_info)
        next_cursor = self._extract_cursor(page_info)

        # make sure we don't request the same page again
        if (
            self._has_next_page
            and CURSOR_VARNAME in self._current_variables
            and next_cursor == self._current_variables[CURSOR_VARNAME]
        ):
            raise GraphQLMissingCursorChange(response.parsed_data)

        self._current_variables[CURSOR_VARNAME] = next_cursor
        return result

    def _get_next_page(self) -> dict[str, Any]:
        response = self._graphql._request(self.query, self._current_variables)
        return self._do_update(response)

    async def _aget_next_page(self) -> dict[str, Any]:
        response = await self._graphql._arequest(self.query, self._current_variables)
        return self._do_update(response)
