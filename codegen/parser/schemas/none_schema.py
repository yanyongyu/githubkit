from typing import TYPE_CHECKING

from ..utils import schema_from_source
from .schema import NoneSchema

if TYPE_CHECKING:
    from ...source import Source


def build_none_schema(source: "Source") -> NoneSchema:
    data = schema_from_source(source)

    return NoneSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
    )
