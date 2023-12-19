from typing import Union

import openapi_pydantic as oas
from pydantic import TypeAdapter

from ...source import Source
from ..data import ResponseData
from ..schemas import parse_schema


def build_response(source: Source, prefix: str) -> ResponseData:
    data = source.data
    try:
        data = TypeAdapter(Union[oas.Reference, oas.Response]).validate_python(data)
    except Exception as e:
        raise TypeError(f"Invalid Response from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.Response.model_validate(source.data)
        except Exception as e:
            raise TypeError(f"Invalid Response from {source.uri}") from e

    response_schema = None
    if data.content:
        media_type = next(
            (type for type in data.content.keys() if "json" in type), None
        ) or next(iter(data.content.keys()))
        response_schema = parse_schema(
            source / "content" / media_type / "schema", prefix
        )

    return ResponseData(description=data.description, response_schema=response_schema)
