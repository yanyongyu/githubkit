import openapi_schema_pydantic as oas

from ...source import Source
from .schema import AnySchema


def build_any_schema(source: Source) -> AnySchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return AnySchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
