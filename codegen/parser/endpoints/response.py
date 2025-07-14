from typing import TYPE_CHECKING

from jsonpointer import JsonPointerException
import openapi_pydantic as oas

from ..data import ResponseData
from ..schemas import parse_schema
from ..utils import type_ref_from_source

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
        # schema may not exist for some media types
        try:
            response_schema = parse_schema(
                source / "content" / media_type / "schema", prefix
            )
        except JsonPointerException:
            response_schema = None

    return ResponseData(description=data.description, response_schema=response_schema)
