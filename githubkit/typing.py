from typing import IO, TYPE_CHECKING, Dict, List, Tuple, Union, TypeVar, Optional

import httpx

T = TypeVar("T")

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

FileContent = Union[IO[bytes], bytes]
FileTypes = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    Tuple[Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    Tuple[Optional[str], FileContent, Optional[str]],
]
