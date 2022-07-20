from typing import Set, Dict, List, Optional, cast

from pydantic import Field
import openapi_schema_pydantic as oas

from . import parse_schema
from ...source import Source
from .property import Property
from .schema import SchemaData
from .. import add_schema, get_schema
from ..utils import sanitize, snake_case, build_class_name, concat_snake_name


class ModelSchema(SchemaData):
    class_name: str
    properties: List[Property] = Field(default_factory=list)
    is_multipart_body: bool = False
    allow_extra: bool = True

    @property
    def required_properties(self) -> List[Property]:
        return [prop for prop in self.properties if prop.required]

    @property
    def optional_properties(self) -> List[Property]:
        return [prop for prop in self.properties if not prop.required]

    def get_model_dependencies(self) -> List["ModelSchema"]:
        return [
            prop.schema_data
            for prop in self.properties
            if isinstance(prop.schema_data, ModelSchema)
        ]

    def get_type_string(self) -> str:
        return self.class_name

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from pydantic import BaseModel")
        return imports


def _process_properties(source: Source, class_name: str) -> List[Property]:
    data = cast(oas.Schema, source.data)

    properties: Dict[str, SchemaData] = {}
    required_set = set(data.required or [])

    def _add_if_no_conflict(name: str, schema: SchemaData):
        if name in properties:
            raise RuntimeError(
                f"Error while creating model {class_name} from {source.uri}, "
                f"duplicated property {name}"
            )
        properties[name] = schema

    for index in range(len(data.allOf or [])):
        prop_source = source / "allOf" / index
        model = parse_schema(
            prop_source, concat_snake_name(class_name, "allof", str(index))
        )
        if not isinstance(model, ModelSchema):
            raise ValueError(
                f"Invalid schema in allOf: {prop_source.uri} from {source.uri}"
            )
        for prop in model.properties:
            _add_if_no_conflict(prop.name, prop.schema_data)

    for name in data.properties or {}:
        prop_source = source / "properties" / name
        prop_schema = parse_schema(
            prop_source, concat_snake_name(class_name, "prop", name)
        )
        _add_if_no_conflict(name, prop_schema)

    return [
        Property(name=name, required=name in required_set, schema_data=schema)
        for name, schema in properties.items()
    ]


def build_model_schema(
    source: Source,
    class_name: str,
) -> ModelSchema:
    data = cast(oas.Schema, source.data)

    class_name = build_class_name(class_name)

    # build and add schema first for cycle/recursive reference
    schema = ModelSchema(
        class_name=class_name,
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
    add_schema(source.uri, schema)

    schema.properties = _process_properties(source, class_name)

    additional_properties = data.additionalProperties
    if isinstance(additional_properties, oas.Reference):
        additional_properties = source.resolve_ref(additional_properties.ref)
    schema.allow_extra = bool(additional_properties)

    return schema
