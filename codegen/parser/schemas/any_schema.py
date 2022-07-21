from typing import cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import AnySchema


def build_any_schema(source: Source) -> AnySchema:
    data = cast(oas.Schema, source.data)
    return AnySchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
