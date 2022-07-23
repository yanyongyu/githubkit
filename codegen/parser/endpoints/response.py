from typing import Optional

from pydantic import BaseModel
import openapi_schema_pydantic as oas

from ...source import Source
from ..schemas import SchemaData, parse_schema


class ResponseData(BaseModel):
    description: str
    response_schema: Optional[SchemaData] = None


def build_response(source: Source, prefix: str) -> ResponseData:
    data = source.data
    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = source.data

    if not isinstance(data, oas.Response):
        raise TypeError(f"Expected Response, got {type(data)} from {source.uri}")

    response_schema = None
    if data.content:
        media_type = next(iter(data.content.keys()))
        response_schema = parse_schema(
            source / "content" / media_type / "media_type_schema", prefix
        )

    return ResponseData(description=data.description, response_schema=response_schema)
