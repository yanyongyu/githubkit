from collections.abc import Callable, Hashable, Mapping, Sequence
from datetime import timedelta
from typing import (
    IO,
    TYPE_CHECKING,
    Annotated,
    Any,
    Literal,
    NamedTuple,
    Optional,
    TypeAlias,
    TypedDict,
    TypeVar,
)

import httpcore
import httpx
from pydantic import Field

from .compat import PYDANTIC_V2
from .exception import GitHubException
from .utils import Unset

if TYPE_CHECKING:
    from hishel._utils import BaseClock

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)

URLTypes: TypeAlias = httpx.URL | str

ProxyTypes: TypeAlias = httpx.URL | str | httpx.Proxy

PrimitiveData: TypeAlias = str | int | float | bool | None
QueryParamTypes: TypeAlias = (
    httpx.QueryParams
    | Mapping[str, PrimitiveData | Sequence[PrimitiveData]]
    | list[tuple[str, PrimitiveData]]
    | tuple[tuple[str, PrimitiveData], ...]
    | str
    | bytes
)

HeaderTypes: TypeAlias = (
    httpx.Headers
    | Mapping[str, str]
    | Mapping[bytes, bytes]
    | Sequence[tuple[str, str]]
    | Sequence[tuple[bytes, bytes]]
)

CookieTypes: TypeAlias = httpx.Cookies | dict[str, str] | list[tuple[str, str]]

ContentTypes: TypeAlias = str | bytes

FileContent: TypeAlias = IO[bytes] | bytes
FileTypes: TypeAlias = (
    FileContent
    | tuple[str | None, FileContent]
    | tuple[str | None, FileContent, str | None]
)
RequestFiles: TypeAlias = Mapping[str, FileTypes] | Sequence[tuple[str, FileTypes]]

if PYDANTIC_V2:  # pragma: pydantic-v2
    from pydantic import AfterValidator
    from pydantic_core import PydanticCustomError

    def _validate_unique_list(value: list[H]) -> list[H]:
        if len(value) != len(set(value)):
            raise PydanticCustomError("unique_list", "value is not a unique list")
        return value

    UniqueList: TypeAlias = Annotated[  # type: ignore
        list[H],
        AfterValidator(_validate_unique_list),
        Field(json_schema_extra={"uniqueItems": True}),
    ]
else:  # pragma: pydantic-v1
    UniqueList: TypeAlias = Annotated[list[H], Field(unique_items=True)]  # type: ignore

UnsetType: TypeAlias = Literal[Unset._UNSET]

# if the property is not required, we allow it to have the value null.
# See https://github.com/yanyongyu/githubkit/issues/47
Missing: TypeAlias = UnsetType | T | None


class RetryOption(NamedTuple):
    do_retry: bool
    retry_after: timedelta | None = None


RetryDecisionFunc: TypeAlias = Callable[[GitHubException, int], RetryOption]


EventHookTypes: TypeAlias = Mapping[str, list[Callable[..., Any]]]


class HishelControllerOptions(TypedDict, total=False):
    """Options for the hishel controller."""

    cacheable_methods: list[str] | None
    cacheable_status_codes: list[int] | None
    cache_private: bool
    allow_heuristics: bool
    clock: Optional["BaseClock"]
    allow_stale: bool
    always_revalidate: bool
    force_cache: bool
    key_generator: Callable[[httpcore.Request, bytes | None], str] | None
