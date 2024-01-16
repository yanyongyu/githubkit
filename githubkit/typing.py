from datetime import timedelta
from typing_extensions import Annotated, TypeAlias
from typing import (
    IO,
    Dict,
    List,
    Tuple,
    Union,
    Literal,
    TypeVar,
    Callable,
    Hashable,
    Optional,
    NamedTuple,
)

import httpx
from pydantic import Field

from .utils import UNSET
from .compat import PYDANTIC_V2
from .exception import GitHubException

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)

URLTypes: TypeAlias = Union[httpx.URL, str]

PrimitiveData: TypeAlias = Optional[Union[str, int, float, bool]]
QueryParamTypes: TypeAlias = Union[
    httpx.QueryParams,
    Dict[str, Union[PrimitiveData, List[PrimitiveData]]],
    List[Tuple[str, PrimitiveData]],
    Tuple[Tuple[str, PrimitiveData], ...],
    str,
    bytes,
]

HeaderTypes: TypeAlias = Union[
    httpx.Headers,
    Dict[str, str],
    Dict[bytes, bytes],
    List[Tuple[str, str]],
    List[Tuple[bytes, bytes]],
]

CookieTypes: TypeAlias = Union[httpx.Cookies, Dict[str, str], List[Tuple[str, str]]]

ContentTypes: TypeAlias = Union[str, bytes]

FileContent: TypeAlias = Union[IO[bytes], bytes]
FileTypes: TypeAlias = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    Tuple[Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    Tuple[Optional[str], FileContent, Optional[str]],
]
RequestFiles: TypeAlias = Union[Dict[str, FileTypes], List[Tuple[str, FileTypes]]]

if PYDANTIC_V2:  # pragma: pydantic-v2
    from pydantic import AfterValidator
    from pydantic_core import PydanticCustomError

    def _validate_unique_list(value: List[H]) -> List[H]:
        if len(value) != len(set(value)):
            raise PydanticCustomError("unique_list", "value is not a unique list")
        return value

    UniqueList: TypeAlias = Annotated[  # type: ignore
        List[H],
        AfterValidator(_validate_unique_list),
        Field(json_schema_extra={"uniqueItems": True}),
    ]
else:  # pragma: pydantic-v1
    UniqueList: TypeAlias = Annotated[List[H], Field(unique_items=True)]  # type: ignore

# if the property is not required, we allow it to have the value null.
# See https://github.com/yanyongyu/githubkit/issues/47
Missing: TypeAlias = Union[Literal[UNSET], T, None]


class RetryOption(NamedTuple):
    do_retry: bool
    retry_after: Optional[timedelta] = None


RetryDecisionFunc: TypeAlias = Callable[[GitHubException, int], RetryOption]
