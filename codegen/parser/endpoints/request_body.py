from typing import Set, List, Union, Literal

import openapi_schema_pydantic as oas
from pydantic import BaseModel, parse_obj_as

from ...source import Source
from ..utils import concat_snake_name
from ..schemas import Property, SchemaData, ModelSchema, UnionSchema, parse_schema


class RequestBodyData(BaseModel):
    type: Literal["form", "json", "file", "raw"]
    body_schema: SchemaData
    required: bool = False

    @property
    def allowed_models(self) -> List[ModelSchema]:
        if isinstance(self.body_schema, ModelSchema):
            return [self.body_schema]
        elif isinstance(self.body_schema, UnionSchema):
            return [
                schema
                for schema in self.body_schema.schemas
                if isinstance(schema, ModelSchema)
            ]
        return []

    def get_raw_definition(self) -> str:
        prop = Property(
            name="data",
            prop_name="data",
            required=self.required,
            schema_data=self.body_schema,
        )
        return prop.get_param_defination()

    def get_endpoint_definition(self) -> str:
        prop = Property(
            name="data",
            prop_name="data",
            required=not bool(self.allowed_models),
            schema_data=self.body_schema,
        )
        return prop.get_param_defination()

    def get_param_imports(self) -> Set[str]:
        imports = set()
        imports.update(self.body_schema.get_param_imports())
        for model in self.allowed_models:
            for prop in model.properties:
                imports.update(prop.get_param_imports())
        return imports

    def get_using_imports(self) -> Set[str]:
        return self.body_schema.get_using_imports()


def build_request_body(source: Source, prefix: str) -> RequestBodyData:
    data = source.data
    try:
        data = parse_obj_as(Union[oas.Reference, oas.RequestBody], data)
    except Exception as e:
        raise TypeError(f"Invalid RequestBody from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.RequestBody.parse_obj(source.data)
        except Exception as e:
            raise TypeError(f"Invalid RequestBody from {source.uri}") from e

    media_types = list(data.content.keys())
    if json_types := [type for type in media_types if "json" in type]:
        json_type = json_types[0]
        return RequestBodyData(
            type="json",
            body_schema=parse_schema(
                source / "content" / json_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif form_types := [type for type in media_types if "form" in type]:
        form_type = form_types[0]
        return RequestBodyData(
            type="form",
            body_schema=parse_schema(
                source / "content" / form_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif file_types := [type for type in media_types if "multipart" in type]:
        file_type = file_types[0]
        return RequestBodyData(
            type="file",
            body_schema=parse_schema(
                source / "content" / file_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif text_types := [type for type in media_types if "text" in type]:
        text_type = text_types[0]
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / text_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif binary_types := [type for type in media_types if "octet-stream" in type]:
        binary_type = binary_types[0]
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / binary_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif "*/*" in media_types:
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / "*/*" / "schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )

    raise RuntimeError(f"Cannot detect body type {media_types} from {source.uri}")
