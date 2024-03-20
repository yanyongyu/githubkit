from typing import TYPE_CHECKING

from .schema import AnySchema
from ..utils import schema_from_source

if TYPE_CHECKING:
    from ...source import Source


def build_any_schema(source: "Source") -> AnySchema:
    data = schema_from_source(source)

    return AnySchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
