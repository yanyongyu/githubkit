from typing import Optional

import openapi_schema_pydantic as oas

from . import parse_schema
from ...source import Source
from .schema import ListSchema
from ..utils import concat_snake_name, schema_from_source


def build_list_schema(
    source: Source, class_name: str, base_source: Optional[Source] = None
) -> ListSchema:
    data = schema_from_source(source)
    base_schema = schema_from_source(base_source) if base_source else None

    return ListSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        item_schema=parse_schema(
            source / "items", concat_snake_name(class_name, "items")
        ),
        min_items=data.minItems or (base_schema and base_schema.minItems),
        max_items=data.maxItems or (base_schema and base_schema.maxItems),
        unique_items=data.uniqueItems or (base_schema and base_schema.uniqueItems),
    )
