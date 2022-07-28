import openapi_schema_pydantic as oas

from ...source import Source
from .schema import BoolSchema


def build_bool_schema(source: Source) -> BoolSchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return BoolSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
