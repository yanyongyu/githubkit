from typing import List, Union, cast

import openapi_schema_pydantic as oas

from . import parse_schema
from ...source import Source
from ..utils import concat_snake_name
from .int_schema import build_int_schema
from .bool_schema import build_bool_schema
from .list_schema import build_list_schema
from .none_schema import build_none_schema
from .schema import SchemaData, UnionSchema
from .float_schema import build_float_schema
from .model_schema import build_model_schema
from .string_schema import build_string_schema


def _build_sub_schema(source: Source, class_name: str) -> List[SchemaData]:
    data = cast(List[Union[oas.Reference, oas.Schema]], source.data)

    schemas: List[SchemaData] = []
    for index in range(len(data)):
        schema_source = source / index
        schema = parse_schema(schema_source, concat_snake_name(class_name, f"{index}"))
        schemas.append(schema)
    return schemas


def build_union_schema(source: Source, class_name: str) -> UnionSchema:
    data = cast(oas.Schema, source.data)

    schemas: List[SchemaData] = []

    if isinstance(data.type, list):
        for type in data.type:
            if type == "null":
                schemas.append(build_none_schema(source))
            elif type == "string":
                schemas.append(build_string_schema(source))
            elif type == "number":
                schemas.append(build_float_schema(source))
            elif type == "integer":
                schemas.append(build_int_schema(source))
            elif type == "boolean":
                schemas.append(build_bool_schema(source))
            elif type == "array":
                schemas.append(build_list_schema(source, class_name))
            elif type == "object":
                schemas.append(build_model_schema(source, class_name))
    if data.anyOf:
        schemas.extend(
            _build_sub_schema(source / "anyOf", concat_snake_name(class_name, "anyof"))
        )
    if data.oneOf:
        schemas.extend(
            _build_sub_schema(source / "oneOf", concat_snake_name(class_name, "oneof"))
        )

    return UnionSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        schemas=schemas,
        discriminator=(data.discriminator and data.discriminator.propertyName),
    )
