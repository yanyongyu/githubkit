from typing import Literal

import openapi_schema_pydantic as oas

from ...source import Source
from ..utils import concat_snake_name
from ..schemas import Property, parse_schema, build_any_schema


class Parameter(Property):
    param_in: Literal["query", "header", "path", "cookie"]


def build_param(source: Source, prefix: str) -> Parameter:
    data = source.data
    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = source.data

    if not isinstance(data, oas.Parameter):
        raise TypeError(f"Expected Parameter, got {type(data)} from {source.uri}")

    if data.param_schema:
        schema = parse_schema(
            source / "param_schema", concat_snake_name(prefix, "param", data.name)
        )
    else:
        schema = build_any_schema(source / "param_schema")

    return Parameter(
        name=data.name,
        required=data.required,
        schema_data=schema,
        param_in=data.param_in,  # type: ignore
    )
