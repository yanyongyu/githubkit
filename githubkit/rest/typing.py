from typing import Dict, List, Tuple, Union, Mapping, Optional

import httpx

URLTypes = Union[httpx.URL, str]

PrimitiveData = Optional[Union[str, int, float, bool]]
QueryParamTypes = Union[
    httpx.QueryParams,
    Mapping[str, Union[PrimitiveData, List[PrimitiveData]]],
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
