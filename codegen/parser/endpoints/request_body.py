from typing import Set, List, Literal

from pydantic import BaseModel
import openapi_schema_pydantic as oas

from ...source import Source
from ..utils import concat_snake_name
from ..schemas import Property, SchemaData, ModelSchema, parse_schema


class RequestBodyData(BaseModel):
    type: Literal["form", "json", "file", "str", "bytes"]
    body_schema: SchemaData
    required: bool = False

    @property
    def is_model(self) -> bool:
        return isinstance(self.body_schema, ModelSchema)

    def get_params_string(self) -> List[str]:
        if not isinstance(self.body_schema, ModelSchema):
            prop = Property(
                name="body",
                prop_name="body",
                required=self.required,
                schema_data=self.body_schema,
            )
            return [prop.get_param_string()]

        results = []
        for prop in self.body_schema.properties:
            ...
        return results

    def get_imports(self) -> Set[str]:
        if isinstance(self.body_schema, ModelSchema):
            return {f"from .models import {self.body_schema.class_name}"}
        return set()


def build_request_body(source: Source, prefix: str) -> RequestBodyData:
    data = source.data
    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = source.data

    if not isinstance(data, oas.RequestBody):
        raise TypeError(f"Expected RequestBody, got {type(data)} from {source.uri}")

    media_types = list(data.content.keys())
    if json_types := [type for type in media_types if "json" in type]:
        json_type = json_types[0]
        return RequestBodyData(
            type="json",
            body_schema=parse_schema(
                source / "content" / json_type / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif form_types := [type for type in media_types if "form" in type]:
        form_type = form_types[0]
        return RequestBodyData(
            type="form",
            body_schema=parse_schema(
                source / "content" / form_type / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif file_types := [type for type in media_types if "multipart" in type]:
        file_type = file_types[0]
        return RequestBodyData(
            type="file",
            body_schema=parse_schema(
                source / "content" / file_type / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif text_types := [type for type in media_types if "text" in type]:
        text_type = text_types[0]
        return RequestBodyData(
            type="str",
            body_schema=parse_schema(
                source / "content" / text_type / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif binary_types := [type for type in media_types if "octet-stream" in type]:
        binary_type = binary_types[0]
        return RequestBodyData(
            type="bytes",
            body_schema=parse_schema(
                source / "content" / binary_type / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )
    elif "*/*" in media_types:
        return RequestBodyData(
            type="bytes",
            body_schema=parse_schema(
                source / "content" / "*/*" / "media_type_schema",
                concat_snake_name(prefix, "body"),
            ),
            required=data.required,
        )

    raise RuntimeError(f"Cannot detect body type {media_types} from {source.uri}")
