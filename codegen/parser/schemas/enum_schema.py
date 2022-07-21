from typing import Any, Dict, List, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import EnumSchema
from ..utils import sanitize, build_class_name


def _values_from_list(values: List[Any]) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    def _add_value(key: str, value: Any):
        if key in output and output[key] != value:
            raise ValueError(f"Duplicate value {key} in enum ", values)
        output[key] = value

    for i, value in enumerate(values):
        if isinstance(value, str):
            key = sanitize(value) if value and value[0].isalpha() else f"VALUE_{value}"
            _add_value(key, value)
            continue
        elif isinstance(value, bool):
            _add_value("TRUE" if value else "FALSE", value)
            continue
        elif isinstance(value, int):
            key = f"VALUE_NEGATIVE_{-value}" if value < 0 else f"VALUE_{value}"
            _add_value(key, value)
            continue
        else:
            _add_value(f"VALUE_{i}", value)
    return output


def build_enum_schema(
    source: Source,
    class_name: str,
) -> EnumSchema:
    data = cast(oas.Schema, source.data)

    class_name = build_class_name(class_name)

    if not data.enum or len(data.enum) == 0:
        raise ValueError("No values provided for Enum", data)

    values = _values_from_list(data.enum)

    return EnumSchema(
        class_name=class_name,
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        values=values,
    )
