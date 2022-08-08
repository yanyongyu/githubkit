from typing import List, Union, Optional

from pydantic import parse_obj_as
import openapi_schema_pydantic as oas

from .. import add_schema
from . import parse_schema
from ...source import Source
from .int_schema import build_int_schema
from .bool_schema import build_bool_schema
from .list_schema import build_list_schema
from .none_schema import build_none_schema
from .float_schema import build_float_schema
from .model_schema import build_model_schema
from .string_schema import build_string_schema
from ..utils import concat_snake_name, schema_from_source
from .schema import (
    AnySchema,
    IntSchema,
    BoolSchema,
    DateSchema,
    FileSchema,
    ListSchema,
    NoneSchema,
    SchemaData,
    FloatSchema,
    ModelSchema,
    UnionSchema,
    StringSchema,
    DateTimeSchema,
)

TYPES_MAP = {
    "null": (NoneSchema,),
    "string": (StringSchema, DateSchema, DateTimeSchema, FileSchema),
    "number": (FloatSchema,),
    "integer": (IntSchema,),
    "boolean": (BoolSchema,),
    "array": (ListSchema,),
    "object": (ModelSchema,),
}


def _build_sub_schema(
    source: Source, class_name: str, base_source: Source
) -> List[SchemaData]:
    data = parse_obj_as(List[Union[oas.Reference, oas.Schema]], source.data)

    schemas: List[SchemaData] = []
    for index in range(len(data)):
        schema_source = source / index
        schema = parse_schema(
            schema_source, concat_snake_name(class_name, f"{index}"), base_source
        )
        if isinstance(schema, UnionSchema):
            schemas.extend(schema.schemas)
        else:
            schemas.append(schema)
    return schemas


def build_union_schema(
    source: Source, class_name: str, base_source: Optional[Source] = None
) -> Union[UnionSchema, AnySchema]:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    schemas: List[SchemaData] = []

    # preprocess for sub schemas
    if data.properties:
        for name in data.properties:
            prop_source = source / "properties" / name
            parse_schema(prop_source, concat_snake_name(class_name, "prop", name))

    if data.anyOf:
        schemas.extend(
            _build_sub_schema(
                source / "anyOf", concat_snake_name(class_name, "anyof"), source
            )
        )
    if data.oneOf:
        schemas.extend(
            _build_sub_schema(
                source / "oneOf", concat_snake_name(class_name, "oneof"), source
            )
        )

    types = data.type or (base_schema and base_schema.type)
    if isinstance(types, list):
        for type in types:
            if type not in TYPES_MAP:
                continue
            types = TYPES_MAP[type]
            if any(isinstance(shema, types) for shema in schemas):
                continue
            if type == "null":
                schemas.append(build_none_schema(source))
            elif type == "string":
                schemas.append(build_string_schema(source, base_source))
            elif type == "number":
                schemas.append(build_float_schema(source, base_source))
            elif type == "integer":
                schemas.append(build_int_schema(source, base_source))
            elif type == "boolean":
                schemas.append(build_bool_schema(source))
            elif type == "array":
                schemas.append(build_list_schema(source, class_name, base_source))
            elif type == "object":
                schema = build_model_schema(
                    source, class_name, base_source, prestore_schema=False
                )
                add_schema((source / "union_object").uri, schema)
                schemas.append(schema)

    if not schemas:
        return AnySchema(
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
        schemas=schemas,
        discriminator=(data.discriminator and data.discriminator.propertyName),
    )
