from typing import Any, Dict, List, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import EnumSchema


def build_enum_schema(source: Source) -> EnumSchema:
    data = cast(oas.Schema, source.data)

    if not data.enum or len(data.enum) == 0:
        raise ValueError("No values provided for Enum", data)

    return EnumSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        values=data.enum,
    )
