from typing import Set, Dict, Optional, cast

from pydantic import Field
import openapi_schema_pydantic as oas

from . import parse_schema
from ...source import Source
from .schema import SchemaData
from ..utils import concat_snake_name


class ListSchema(SchemaData):
    item_schema: SchemaData
    min_items: Optional[int] = Field(default=None, ge=0)
    max_items: Optional[int] = Field(default=None, ge=0)
    unique_items: Optional[bool] = None

    def get_type_string(self) -> str:
        return f"List[{self.item_schema.get_type_string()}]"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from typing import List")
        return imports

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
        if self.max_items is not None:
            args["max_items"] = repr(self.max_items)
        if self.min_items is not None:
            args["min_items"] = repr(self.min_items)
        if self.unique_items is not None:
            args["unique_items"] = repr(self.unique_items)
        return args


def build_list_schema(source: Source, class_name: str) -> ListSchema:
    data = cast(oas.Schema, source.data)
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
