from typing import Union

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import EnumSchema, NoneSchema, UnionSchema


def build_enum_schema(source: Source) -> Union[EnumSchema, UnionSchema]:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    if not data.enum or len(data.enum) == 0:
        raise ValueError("No values provided for Enum", data)

    if None in data.enum:
        values = data.enum.copy()
        values.remove(None)
        return UnionSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            schemas=[
                NoneSchema(),
                EnumSchema(
                    title=data.title,
                    description=data.description,
                    default=data.default,
                    examples=data.examples or (data.example and [data.example]),
                    values=values,
                ),
            ],
        )

    return EnumSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        values=data.enum,
    )
