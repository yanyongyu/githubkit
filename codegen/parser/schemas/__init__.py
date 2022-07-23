import openapi_schema_pydantic as oas

from ...source import Source
from .schema import Property as Property
from .schema import AnySchema as AnySchema
from .schema import IntSchema as IntSchema
from .schema import BoolSchema as BoolSchema
from .schema import DateSchema as DateSchema
from .schema import EnumSchema as EnumSchema
from .schema import FileSchema as FileSchema
from .schema import ListSchema as ListSchema
from .schema import NoneSchema as NoneSchema
from .schema import SchemaData as SchemaData
from .schema import FloatSchema as FloatSchema
from .schema import ModelSchema as ModelSchema
from .schema import UnionSchema as UnionSchema
from .schema import StringSchema as StringSchema
from .. import add_schema, get_schema, get_schemas
from .schema import DateTimeSchema as DateTimeSchema


def parse_schema(source: Source, class_name: str) -> SchemaData:
    data = source.data
    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = source.data
        class_name = source.pointer.parts[-1]
    if not isinstance(data, oas.Schema):
        raise TypeError(f"Expected Schema, got {type(data)} from {source.uri}")

    if exist := get_schema(source.uri):
        return exist

    schema_type = (
        (data.type[0] if len(data.type) == 1 else data.type)
        if isinstance(data.type, list)
        else data.type
    )

    if data.enum:
        schema = build_enum_schema(source)
    elif isinstance(data.type, list) or data.anyOf or data.oneOf:
        schema = build_union_schema(source, class_name)
    elif schema_type == "null":
        schema = build_none_schema(source)
    elif schema_type == "string":
        schema = build_string_schema(source)
    elif schema_type == "number":
        schema = build_float_schema(source)
    elif schema_type == "integer":
        schema = build_int_schema(source)
    elif schema_type == "boolean":
        schema = build_bool_schema(source)
    elif schema_type == "array":
        schema = build_list_schema(source, class_name)
    elif schema_type == "object" or data.allOf:
        schema = build_model_schema(source, class_name)
    else:
        schema = build_any_schema(source)

    if source.uri not in get_schemas():
        add_schema(source.uri, schema)
    return schema


from .any_schema import build_any_schema
from .int_schema import build_int_schema
from .bool_schema import build_bool_schema
from .enum_schema import build_enum_schema
from .list_schema import build_list_schema
from .none_schema import build_none_schema
from .float_schema import build_float_schema
from .model_schema import build_model_schema
from .union_schema import build_union_schema
from .string_schema import build_string_schema
