import openapi_schema_pydantic as oas

from . import parse_schema
from ...source import Source
from .schema import ListSchema
from ..utils import concat_snake_name


def build_list_schema(source: Source, class_name: str) -> ListSchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return ListSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        item_schema=parse_schema(
            source / "items", concat_snake_name(class_name, "items")
        ),
        min_items=data.minItems,
        max_items=data.maxItems,
        unique_items=data.uniqueItems,
    )
