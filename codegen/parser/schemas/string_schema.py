from typing import TYPE_CHECKING

from ..utils import schema_from_source
from .schema import DateSchema, DateTimeSchema, EnumSchema, FileSchema, StringSchema

if TYPE_CHECKING:
    from ...source import Source


def build_string_schema(
    source: "Source",
    base_source: "Source | None" = None,
) -> StringSchema | EnumSchema | DateSchema | DateTimeSchema | FileSchema:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    schema_format = data.schema_format or (base_schema and base_schema.schema_format)
    max_length = (
        (base_schema and base_schema.maxLength)
        if data.maxLength is None
        else data.maxLength
    )
    min_length = (
        (base_schema and base_schema.minLength)
        if data.minLength is None
        else data.minLength
    )

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
    # special case
    elif max_length == 0:
        return EnumSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            values=[""],
        )
    else:
        return StringSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            min_length=min_length,
            max_length=max_length,
            pattern=data.pattern or (base_schema and base_schema.pattern),
        )
