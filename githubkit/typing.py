from typing import IO, Dict, List, Tuple, Union, TypeVar, Hashable, Optional, Annotated

import httpx
from pydantic import Field, AfterValidator
from pydantic_core import PydanticCustomError

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)

URLTypes = Union[httpx.URL, str]

PrimitiveData = Optional[Union[str, int, float, bool]]
QueryParamTypes = Union[
    httpx.QueryParams,
    Dict[str, Union[PrimitiveData, List[PrimitiveData]]],
    List[Tuple[str, PrimitiveData]],
    Tuple[Tuple[str, PrimitiveData], ...],
    str,
    bytes,
]

HeaderTypes = Union[
    httpx.Headers,
    Dict[str, str],
    Dict[bytes, bytes],
    List[Tuple[str, str]],
    List[Tuple[bytes, bytes]],
]

CookieTypes = Union[httpx.Cookies, Dict[str, str], List[Tuple[str, str]]]

ContentTypes = Union[str, bytes]

FileContent = Union[IO[bytes], bytes]
FileTypes = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    Tuple[Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    Tuple[Optional[str], FileContent, Optional[str]],
]
RequestFiles = Union[Dict[str, FileTypes], List[Tuple[str, FileTypes]]]


def validate_unique_list(value: List[H]) -> List[H]:
    if len(value) != len(set(value)):
        raise PydanticCustomError("unique_list", "value is not a unique list")
    return value


UniqueList = Annotated[
    List[H],
    AfterValidator(validate_unique_list),
    Field(json_schema_extra={"uniqueItems": True}),
]
