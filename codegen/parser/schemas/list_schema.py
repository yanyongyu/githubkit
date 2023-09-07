from typing import Union, Optional

from . import parse_schema
from ...source import Source
from .schema import ListSchema, UniqueListSchema
from ..utils import concat_snake_name, schema_from_source


def build_list_schema(
    source: Source, class_name: str, base_source: Optional[Source] = None
) -> Union[ListSchema, UniqueListSchema]:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    if data.uniqueItems or (base_schema and base_schema.uniqueItems):
        schema_class = UniqueListSchema
    else:
        schema_class = ListSchema

    return schema_class(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        item_schema=parse_schema(
            source / "items", concat_snake_name(class_name, "items")
        ),
        min_length=data.minItems or (base_schema and base_schema.minItems),
        max_length=data.maxItems or (base_schema and base_schema.maxItems),
    )
