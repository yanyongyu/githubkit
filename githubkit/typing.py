from collections.abc import Hashable, Mapping, Sequence
from datetime import timedelta
from typing import (
    IO,
    Annotated,
    Callable,
    Literal,
    NamedTuple,
    Optional,
    TypeVar,
    Union,
)
from typing_extensions import TypeAlias

import httpx
from pydantic import Field

from .compat import PYDANTIC_V2
from .exception import GitHubException
from .utils import Unset

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)

URLTypes: TypeAlias = Union[httpx.URL, str]

PrimitiveData: TypeAlias = Optional[Union[str, int, float, bool]]
QueryParamTypes: TypeAlias = Union[
    httpx.QueryParams,
    Mapping[str, Union[PrimitiveData, Sequence[PrimitiveData]]],
    list[tuple[str, PrimitiveData]],
    tuple[tuple[str, PrimitiveData], ...],
    str,
    bytes,
]

HeaderTypes: TypeAlias = Union[
    httpx.Headers,
    Mapping[str, str],
    Mapping[bytes, bytes],
    Sequence[tuple[str, str]],
    Sequence[tuple[bytes, bytes]],
]

CookieTypes: TypeAlias = Union[httpx.Cookies, dict[str, str], list[tuple[str, str]]]

ContentTypes: TypeAlias = Union[str, bytes]

FileContent: TypeAlias = Union[IO[bytes], bytes]
FileTypes: TypeAlias = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    tuple[Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    tuple[Optional[str], FileContent, Optional[str]],
]
RequestFiles: TypeAlias = Union[
    Mapping[str, FileTypes], Sequence[tuple[str, FileTypes]]
]

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
Missing: TypeAlias = Union[UnsetType, T, None]


class RetryOption(NamedTuple):
    do_retry: bool
    retry_after: Optional[timedelta] = None


RetryDecisionFunc: TypeAlias = Callable[[GitHubException, int], RetryOption]
