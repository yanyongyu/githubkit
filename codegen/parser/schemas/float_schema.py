from typing import TYPE_CHECKING

from ..utils import schema_from_source
from .schema import FloatSchema

if TYPE_CHECKING:
    from ...source import Source


def build_float_schema(
    source: "Source", base_source: "Source | None" = None
) -> FloatSchema:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    return FloatSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        multiple_of=data.multipleOf or (base_schema and base_schema.multipleOf),
        maximum=data.maximum or (base_schema and base_schema.maximum),
        exclusive_maximum=(
            data.exclusiveMaximum or (base_schema and base_schema.exclusiveMaximum)
        ),
        minimum=data.minimum or (base_schema and base_schema.minimum),
        exclusive_minimum=(
            data.exclusiveMinimum or (base_schema and base_schema.exclusiveMinimum)
        ),
    )
