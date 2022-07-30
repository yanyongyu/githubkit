from typing import Union

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import EnumSchema, NoneSchema, UnionSchema


def build_enum_schema(source: Source) -> Union[EnumSchema, UnionSchema, NoneSchema]:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    if data.const is not None:
        values = [data.const]
    elif data.enum:
        values = data.enum
    else:
        raise ValueError("No values provided for Enum", data)

    if None in values:
        values = values.copy()
        values.remove(None)
        if not values:
            return NoneSchema(
                title=data.title,
                description=data.description,
                default=data.default,
                examples=data.examples or (data.example and [data.example]),
            )
        return UnionSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            schemas=[
                NoneSchema(
                    title=data.title,
                    description=data.description,
                    default=data.default,
                    examples=data.examples or (data.example and [data.example]),
                ),
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
        values=values,
    )
