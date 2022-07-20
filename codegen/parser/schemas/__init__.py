import openapi_schema_pydantic as oas

from ...source import Source
from .property import Property as Property
from .schema import SchemaData as SchemaData
from .. import add_schema, get_schema, get_schemas


def parse_schema(source: Source, class_name: str) -> SchemaData:
    data = source.data
    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = source.data
        class_name = source.pointer.parts[-1]
    if not isinstance(data, oas.Schema):
        raise TypeError(f"Expected Schema, got {type(data)} from {source.uri}")

    exist = get_schema(source.uri)
    if exist:
        return exist

    if data.enum:
        schema = build_enum_schema(source, class_name)
    elif isinstance(data.type, list) or data.anyOf or data.oneOf:
        schema = build_union_schema(source, class_name)
    elif data.type == "null":
        schema = build_none_schema(source)
    elif data.type == "string":
        schema = build_string_schema(source)
    elif data.type == "number":
        schema = build_float_schema(source)
    elif data.type == "integer":
        schema = build_int_schema(source)
    elif data.type == "boolean":
        schema = build_bool_schema(source)
    elif data.type == "array":
        schema = build_list_schema(source, class_name)
    elif data.type == "object" or data.allOf:
        schema = build_model_schema(source, class_name)
    else:
        schema = build_any_schema(source)

    if source.uri not in get_schemas():
        add_schema(source.uri, schema)
    return schema


def parse_property(source: Source, name: str, required: bool) -> Property:
    return Property(
        name=name, required=required, schema_data=parse_schema(source, name)
    )


from .any_schema import build_any_schema
from .int_schema import build_int_schema
from .bool_schema import build_bool_schema
from .enum_schema import build_enum_schema
from .list_schema import build_list_schema
from .none_schema import build_none_schema
from .float_schema import build_float_schema
from .model_schema import build_model_schema
from .union_schema import build_union_schema
from .any_schema import AnySchema as AnySchema
from .int_schema import IntSchema as IntSchema
from .string_schema import build_string_schema
from .bool_schema import BoolSchema as BoolSchema
from .enum_schema import EnumSchema as EnumSchema
from .list_schema import ListSchema as ListSchema
from .none_schema import NoneSchema as NoneSchema
from .string_schema import DateSchema as DateSchema
from .string_schema import FileSchema as FileSchema
from .float_schema import FloatSchema as FloatSchema
from .model_schema import ModelSchema as ModelSchema
from .union_schema import UnionSchema as UnionSchema
from .string_schema import StringSchema as StringSchema
from .string_schema import DateTimeSchema as DateTimeSchema
