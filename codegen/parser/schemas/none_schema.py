import openapi_schema_pydantic as oas

from ...source import Source
from .schema import NoneSchema


def build_none_schema(source: Source) -> NoneSchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return NoneSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
