from typing import Union, Optional

import openapi_schema_pydantic as oas

from ...source import Source
from ..utils import schema_from_source
from .schema import DateSchema, FileSchema, StringSchema, DateTimeSchema


def build_string_schema(
    source: Source,
    base_source: Optional[Source] = None,
) -> Union[StringSchema, DateSchema, DateTimeSchema, FileSchema]:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    schema_format = data.schema_format or (base_schema and base_schema.schema_format)

    if schema_format == "date-time":
        return DateTimeSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif schema_format == "date":
        return DateSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif schema_format == "binary":
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
            min_length=data.minLength or (base_schema and base_schema.minLength),
            max_length=data.maxLength or (base_schema and base_schema.maxLength),
            pattern=data.pattern or (base_schema and base_schema.pattern),
        )
