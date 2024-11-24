from typing import TYPE_CHECKING

import openapi_pydantic as oas

from ..data import RequestBodyData
from ..schemas import parse_schema
from ..utils import concat_snake_name, type_ref_from_source

if TYPE_CHECKING:
    from ...source import Source


DEFAULT_JSON_CONTENT_TYPE = "application/json"
DEFAULT_FORM_CONTENT_TYPE = "application/x-www-form-urlencoded"
DEFAULT_MULTIPART_CONTENT_TYPE = "multipart/form-data"
DEFAULT_TEXT_CONTENT_TYPE = "text/plain"
DEFAULT_BINARY_CONTENT_TYPE = "application/octet-stream"


def build_request_body(source: "Source", prefix: str) -> RequestBodyData:
    data = type_ref_from_source(source, oas.RequestBody)

    while isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = type_ref_from_source(source, oas.RequestBody)

    media_types = list(data.content.keys())
    if json_types := [type for type in media_types if "json" in type]:
        json_type = (
            DEFAULT_JSON_CONTENT_TYPE
            if DEFAULT_JSON_CONTENT_TYPE in json_types
            else json_types[0]
        )
        return RequestBodyData(
            type="json",
            body_schema=parse_schema(
                source / "content" / json_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=json_type,
            required=data.required,
        )
    elif file_types := [type for type in media_types if "multipart" in type]:
        file_type = (
            DEFAULT_MULTIPART_CONTENT_TYPE
            if DEFAULT_MULTIPART_CONTENT_TYPE in file_types
            else file_types[0]
        )
        return RequestBodyData(
            type="file",
            body_schema=parse_schema(
                source / "content" / file_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=file_type,
            required=data.required,
        )
    elif form_types := [type for type in media_types if "form" in type]:
        form_type = (
            DEFAULT_FORM_CONTENT_TYPE
            if DEFAULT_FORM_CONTENT_TYPE in form_types
            else form_types[0]
        )
        return RequestBodyData(
            type="form",
            body_schema=parse_schema(
                source / "content" / form_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=form_type,
            required=data.required,
        )
    elif text_types := [type for type in media_types if "text" in type]:
        text_type = (
            DEFAULT_TEXT_CONTENT_TYPE
            if DEFAULT_TEXT_CONTENT_TYPE in text_types
            else text_types[0]
        )
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / text_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=text_type,
            required=data.required,
        )
    elif binary_types := [type for type in media_types if "octet-stream" in type]:
        binary_type = (
            DEFAULT_BINARY_CONTENT_TYPE
            if DEFAULT_BINARY_CONTENT_TYPE in binary_types
            else binary_types[0]
        )
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / binary_type / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=binary_type,
            required=data.required,
        )
    elif "*/*" in media_types:
        return RequestBodyData(
            type="raw",
            body_schema=parse_schema(
                source / "content" / "*/*" / "schema",
                concat_snake_name(prefix, "body"),
            ),
            content_type=None,
            required=data.required,
        )

    raise RuntimeError(f"Cannot detect body type {media_types} from {source.uri}")
