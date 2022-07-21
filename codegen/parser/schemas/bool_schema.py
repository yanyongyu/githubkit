from typing import cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import BoolSchema


def build_bool_schema(source: Source) -> BoolSchema:
    data = cast(oas.Schema, source.data)
    return BoolSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
