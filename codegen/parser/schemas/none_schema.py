from typing import ClassVar, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import SchemaData


class NoneSchema(SchemaData):
    _type_string: ClassVar[str] = "None"


def build_none_schema(source: Source) -> NoneSchema:
    data = cast(oas.Schema, source.data)
    return NoneSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
