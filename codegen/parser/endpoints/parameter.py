from typing import TYPE_CHECKING

import openapi_pydantic as oas

from ..data import Parameter
from ..utils import build_prop_name, concat_snake_name, type_ref_from_source
from ..schemas import parse_schema, build_any_schema

if TYPE_CHECKING:
    from ...source import Source


def build_param(source: "Source", prefix: str) -> Parameter:
    data = type_ref_from_source(source, oas.Parameter)

    while isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        data = type_ref_from_source(source, oas.Parameter)

    if data.param_schema:
        schema = parse_schema(
            source / "schema", concat_snake_name(prefix, "param", data.name)
        )
    else:
        schema = build_any_schema(source / "schema")

    return Parameter(
        name=data.name,
        prop_name=build_prop_name(data.name),
        required=data.required,
        schema_data=schema,
        param_in=data.param_in.value,
    )
