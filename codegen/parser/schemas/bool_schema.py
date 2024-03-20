from ...source import Source
from .schema import BoolSchema
from ..utils import build_boolean, schema_from_source


def build_bool_schema(source: Source) -> BoolSchema:
    data = schema_from_source(source)

    return BoolSchema(
        title=data.title,
        description=data.description,
        default=build_boolean(data.default) if data.default is not None else None,
        examples=data.examples or (data.example and [data.example]),
    )
