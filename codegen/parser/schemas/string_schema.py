from typing import Union, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import DateSchema, FileSchema, StringSchema, DateTimeSchema


def build_string_schema(
    source: Source,
) -> Union[StringSchema, DateSchema, DateTimeSchema, FileSchema]:
    data = cast(oas.Schema, source.data)
    if data.schema_format == "date-time":
        return DateTimeSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif data.schema_format == "date":
        return DateSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif data.schema_format == "binary":
        return FileSchema(
            title=data.title,
            description=data.description,
            default=None,
            examples=data.examples or (data.example and [data.example]),
        )
    else:
        return StringSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            min_length=data.minLength,
            max_length=data.maxLength,
            pattern=data.pattern,
        )
