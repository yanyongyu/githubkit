from typing import ClassVar, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .property import SchemaData


class AnySchema(SchemaData):
    _type_string: ClassVar[str] = "Any"


def build_any_schema(source: Source) -> AnySchema:
    data = cast(oas.Schema, source.data)
    return AnySchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
