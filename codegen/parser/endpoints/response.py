from typing import TYPE_CHECKING

import openapi_pydantic as oas

from ..data import ResponseData
from ..utils import type_ref_from_source
from ..schemas import parse_schema

if TYPE_CHECKING:
    from ...source import Source


def build_response(source: "Source", prefix: str) -> ResponseData:
    data = type_ref_from_source(source, oas.Response)

    while isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = type_ref_from_source(source, oas.Response)

    response_schema = None
    if data.content:
        media_type = next(
            (type for type in data.content.keys() if "json" in type), None
        ) or next(iter(data.content.keys()))
        response_schema = parse_schema(
            source / "content" / media_type / "schema", prefix
        )

    return ResponseData(description=data.description, response_schema=response_schema)
