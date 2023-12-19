from typing import Union

import openapi_pydantic as oas
from pydantic import TypeAdapter

from ...source import Source
from ..data import Parameter
from ..schemas import parse_schema, build_any_schema
from ..utils import build_prop_name, concat_snake_name


def build_param(source: Source, prefix: str) -> Parameter:
    data = source.data
    try:
        data = TypeAdapter(Union[oas.Reference, oas.Parameter]).validate_python(data)
    except Exception as e:
        raise TypeError(f"Invalid Parameter from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.Parameter.model_validate(source.data)
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
        param_in=data.param_in.value,
    )
