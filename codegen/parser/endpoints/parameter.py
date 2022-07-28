from typing import Union, Literal

from pydantic import parse_obj_as
import openapi_schema_pydantic as oas

from ...source import Source
from ..utils import build_prop_name, concat_snake_name
from ..schemas import Property, parse_schema, build_any_schema


class Parameter(Property):
    param_in: Literal["query", "header", "path", "cookie"]


def build_param(source: Source, prefix: str) -> Parameter:
    data = source.data
    try:
        data = parse_obj_as(Union[oas.Reference, oas.Parameter], data)
    except Exception as e:
        raise TypeError(f"Invalid Parameter from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.Parameter.parse_obj(source.data)
        except Exception as e:
            raise TypeError(f"Invalid Parameter from {source.uri}") from e

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
        param_in=data.param_in,  # type: ignore
    )
