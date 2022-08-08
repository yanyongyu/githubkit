from typing import Union, Optional

import openapi_schema_pydantic as oas

from ...source import Source
from ..utils import schema_from_source
from .schema import EnumSchema, NoneSchema, UnionSchema


def build_enum_schema(
    source: Source, base_source: Optional[Source] = None
) -> Union[EnumSchema, UnionSchema, NoneSchema]:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    if data.const is not None:
        values = [data.const]
    elif data.enum:
        values = data.enum
    elif base_schema and base_schema.const is not None:
        values = [base_schema.const]
    elif base_schema and base_schema.enum:
        values = base_schema.enum
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
