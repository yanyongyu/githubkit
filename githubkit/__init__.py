from functools import cached_property
from typing_extensions import ParamSpec
from typing import Any, Dict, List, Union, TypeVar, Callable, Optional, Awaitable

from .core import GitHubCore
from .rest import RestNamespace
from .response import Response as Response
from .paginator import Paginator as Paginator
from .auth import BasicAuthStrategy as BasicAuthStrategy
from .auth import TokenAuthStrategy as TokenAuthStrategy

RT = TypeVar("RT")
CP = ParamSpec("CP")


class GitHub(GitHubCore):
    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)

    def graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Response[Any]:
        json: Dict[str, Any] = {"query": query}
        if variables:
            json["variables"] = variables

        return self.request("POST", "/graphql", json=json)

    async def async_graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Response[Any]:
        json: Dict[str, Any] = {"query": query}
        if variables:
            json["variables"] = variables

        return await self.arequest("POST", "/graphql", json=json)

    @staticmethod
    def paginate(
        request: Union[
            Callable[CP, Response[List[RT]]],
            Callable[CP, Awaitable[Response[List[RT]]]],
        ],
        page: int = 1,
        per_page: int = 100,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        return Paginator(request, page, per_page, *args, **kwargs)
