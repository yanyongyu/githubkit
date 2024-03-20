from typing import TYPE_CHECKING, TypeVar

import openapi_pydantic as oas

from .. import add_schema
from . import parse_schema
from ..utils import (
    build_prop_name,
    build_class_name,
    concat_snake_name,
    schema_from_source,
)
from .schema import (
    Property,
    IntSchema,
    BoolSchema,
    DateSchema,
    EnumSchema,
    FileSchema,
    ListSchema,
    NoneSchema,
    SchemaData,
    FloatSchema,
    ModelSchema,
    UnionSchema,
    StringSchema,
    DateTimeSchema,
    UniqueListSchema,
)

if TYPE_CHECKING:
    from ...source import Source

ST = TypeVar("ST", bound=SchemaData)


def _is_nullable(schema: SchemaData) -> bool:
    if isinstance(schema, NoneSchema):
        return True
    if not isinstance(schema, UnionSchema):
        return False
    return any(isinstance(schema, NoneSchema) for schema in schema.schemas)


def _find_schema(
    schema: SchemaData, type: type[ST] | tuple[type[ST], ...]
) -> ST | None:
    if isinstance(schema, type):
        return schema
    if isinstance(schema, UnionSchema):
        for schema in schema.schemas:
            # FIXME: maybe multiple enum schemas in union (oneOf)
            if isinstance(schema, type):
                return schema


def _is_union_subset(first: SchemaData, second: SchemaData) -> SchemaData | None:
    first_schemas = first.schemas if isinstance(first, UnionSchema) else [first]
    second_schemas = second.schemas if isinstance(second, UnionSchema) else [second]
    one_schemas = (
        first_schemas if len(first_schemas) <= len(second_schemas) else second_schemas
    )
    another_schemas = (
        second_schemas if len(first_schemas) <= len(second_schemas) else first_schemas
    )
    for schema in one_schemas:
        if all(schema != another_schema for another_schema in another_schemas):
            return
    return first if len(first_schemas) <= len(second_schemas) else second


def _is_type_subset(enum: EnumSchema, schema: SchemaData) -> EnumSchema | None:
    if enum.is_str_enum and _find_schema(schema, StringSchema):
        return enum
    elif enum.is_bool_enum and _find_schema(schema, BoolSchema):
        return enum
    elif enum.is_int_enum and _find_schema(schema, IntSchema):
        return enum
    elif enum.is_float_enum and _find_schema(schema, FloatSchema):
        return enum


def _is_enum_subset(first: SchemaData, second: SchemaData) -> EnumSchema | None:
    first_schema = _find_schema(first, EnumSchema)
    second_schema = _find_schema(second, EnumSchema)

    # both enum, check value subset
    if first_schema and second_schema:
        first_values = set(first_schema.values)
        second_values = set(second_schema.values)
        if first_values.issubset(second_values):
            return first_schema
        elif second_values.issubset(first_values):
            return second_schema

    # first enum, check type subset
    if first_schema and (schema := _is_type_subset(first_schema, second)):
        return schema

    # second enum, check type subset
    if second_schema and (schema := _is_type_subset(second_schema, first)):
        return schema


def _is_string_subset(
    first: SchemaData, second: SchemaData
) -> DateSchema | DateTimeSchema | FileSchema | None:
    first_schema = _find_schema(first, StringSchema)
    second_schema = _find_schema(second, (DateSchema, DateTimeSchema, FileSchema))
    return first_schema and second_schema


def _is_model_merge(
    source: "Source", name: str, prefix: str, first: SchemaData, second: SchemaData
) -> ModelSchema | None:
    if (first_model := _find_schema(first, ModelSchema)) and (
        second_model := _find_schema(second, ModelSchema)
    ):
        properties = {prop.name: prop for prop in first_model.properties}
        class_name = build_class_name(prefix)

        for prop in second_model.properties:
            if prop.name in properties:
                # try merge
                try:
                    prop = _merge_property(
                        source / "allof" / "merged" / name,
                        properties[prop.name],
                        prop,
                        concat_snake_name(class_name, "prop", prop.name),
                    )
                except Exception as e:
                    raise RuntimeError(
                        f"Error while creating model {class_name}, "
                        f"duplicated property {prop.name}"
                    ) from e
            properties[prop.name] = prop

        schema = ModelSchema(
            class_name=class_name,
            properties=list(properties.values()),
            allow_extra=first_model.allow_extra and second_model.allow_extra,
        )
        add_schema((source / "allof" / "merged" / name).uri, schema)
        return schema


def _is_list_merge(
    source: "Source", name: str, prefix: str, first: SchemaData, second: SchemaData
) -> ListSchema | None:
    if isinstance(first, ListSchema) and isinstance(second, ListSchema):
        return ListSchema(
            title=first.title,
            description=first.description,
            default=first.default,
            examples=first.examples,
            item_schema=_merge_schema(
                source, name, prefix, first.item_schema, second.item_schema
            ),
        )


def _is_unique_list_merge(
    source: "Source", name: str, prefix: str, first: SchemaData, second: SchemaData
) -> UniqueListSchema | None:
    if (
        (isinstance(first, UniqueListSchema) and isinstance(second, ListSchema))
        or (isinstance(first, ListSchema) and isinstance(second, UniqueListSchema))
        or (
            isinstance(first, UniqueListSchema) and isinstance(second, UniqueListSchema)
        )
    ):
        return UniqueListSchema(
            title=first.title,
            description=first.description,
            default=first.default,
            examples=first.examples,
            item_schema=_merge_schema(
                source, name, prefix, first.item_schema, second.item_schema
            ),
        )


def _merge_schema(
    source: "Source", name: str, prefix: str, first: SchemaData, second: SchemaData
):
    if schema := (
        _is_union_subset(first, second)
        or _is_string_subset(first, second)
        or _is_string_subset(second, first)
        or _is_enum_subset(first, second)
        or _is_model_merge(source, name, prefix, first, second)
        or _is_list_merge(source, name, prefix, first, second)
        or _is_unique_list_merge(source, name, prefix, first, second)
    ):
        return schema
    raise RuntimeError(f"Cannot merge schema for {name}: {first!r}; {second!r}")


def _merge_property(
    source: "Source", first: Property, second: Property, prefix: str
) -> Property:
    if first.name != second.name:
        raise ValueError(f"Property with different name: {first.name} != {second.name}")

    required = first.required or second.required
    nullable = _is_nullable(first.schema_data) and _is_nullable(second.schema_data)

    schema = _merge_schema(
        source, first.name, prefix, first.schema_data, second.schema_data
    )
    if nullable:
        schema = UnionSchema(
            title=schema.title,
            description=schema.description,
            default=schema.default,
            examples=schema.examples,
            schemas=[schema, NoneSchema()],
        )
    return Property(
        name=second.name,
        prop_name=second.prop_name,
        required=required,
        schema_data=schema,
    )


def _process_properties(
    source: "Source", class_name: str, base_source: "Source | None" = None
) -> list[Property]:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    properties: dict[str, Property] = {}
    required_set = set(data.required or [])
    if base_schema and base_schema.required:
        required_set.update(base_schema.required)

    def _add_if_no_conflict(prop: Property):
        if prop.name in properties:
            # try merge
            try:
                prop = _merge_property(
                    source,
                    properties[prop.name],
                    prop,
                    concat_snake_name(class_name, "merged", prop.name),
                )
            except Exception as e:
                raise RuntimeError(
                    f"Error while creating model {class_name} from {source.uri}, "
                    f"duplicated property {prop.name}"
                ) from e
        properties[prop.name] = prop

    for index in range(len(data.allOf or [])):
        prop_source = source / "allOf" / index
        model = parse_schema(
            prop_source, concat_snake_name(class_name, "allof", str(index))
        )
        if isinstance(model, UnionSchema):
            assertion = [isinstance(schema, ModelSchema) for schema in model.schemas]
            if True in assertion:
                model = model.schemas[assertion.index(True)]
        if not isinstance(model, ModelSchema):
            raise ValueError(
                f"Invalid schema {model!r} in allOf: "
                f"{prop_source.uri} from {source.uri}"
            )
        for prop in model.properties:
            _add_if_no_conflict(prop)
    if base_source and base_schema and base_schema.properties:
        for name in base_schema.properties:
            prop_source = base_source / "properties" / name
            prop_schema = parse_schema(
                prop_source, concat_snake_name(class_name, "prop", name)
            )
            _add_if_no_conflict(
                Property(
                    name=name,
                    prop_name=build_prop_name(name),
                    required=name in required_set,
                    schema_data=prop_schema,
                )
            )

    if data.properties:
        for name in data.properties:
            prop_source = source / "properties" / name
            prop_schema = parse_schema(
                prop_source, concat_snake_name(class_name, "prop", name)
            )
            _add_if_no_conflict(
                Property(
                    name=name,
                    prop_name=build_prop_name(name),
                    required=name in required_set,
                    schema_data=prop_schema,
                )
            )
    return list(properties.values())


def build_model_schema(
    source: "Source",
    class_name: str,
    base_source: "Source | None" = None,
    prestore_schema: bool = True,
) -> ModelSchema:
    data = schema_from_source(source)

    class_name = build_class_name(class_name)

    # build and add schema first for cycle/recursive reference
    schema = ModelSchema(
        class_name=class_name,
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
    if prestore_schema:
        add_schema(source.uri, schema)

    schema.properties = _process_properties(source, class_name, base_source)

    additional_properties = data.additionalProperties
    if isinstance(additional_properties, oas.Reference):
        additional_properties = source.resolve_ref(additional_properties.ref)
    schema.allow_extra = bool(additional_properties)

    return schema
