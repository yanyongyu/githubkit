from typing import Union

import openapi_pydantic as oas
from pydantic import TypeAdapter

from ...source import Source
from ..data import RequestBodyData
from ..schemas import parse_schema
from ..utils import concat_snake_name


def build_request_body(source: Source, prefix: str) -> RequestBodyData:
    data = source.data
    try:
        data = TypeAdapter(Union[oas.Reference, oas.RequestBody]).validate_python(data)
    except Exception as e:
        raise TypeError(f"Invalid RequestBody from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.RequestBody.model_validate(source.data)
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
