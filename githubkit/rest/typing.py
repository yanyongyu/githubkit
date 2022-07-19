from typing import TYPE_CHECKING, Dict, List, Tuple, Union, TypeVar, Optional

import httpx

if TYPE_CHECKING:
    from .response import Response

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

ResponseModelTypes = Dict[int, Dict[str, "Response[T]"]]
