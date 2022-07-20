from typing import Set, Dict, Union, ClassVar, Optional, cast

from pydantic import Field
import openapi_schema_pydantic as oas

from .. import add_schema
from ...source import Source
from .schema import SchemaData


class StringSchema(SchemaData):
    min_length: Optional[int] = Field(default=None, ge=0)
    max_length: Optional[int] = Field(default=None, ge=0)
    pattern: Optional[str] = None

    _type_string: ClassVar[str] = "str"

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args() or {}
        if self.min_length is not None:
            args["min_length"] = str(self.min_length)
        if self.max_length is not None:
            args["max_length"] = str(self.max_length)
        if self.pattern is not None:
            args["regex"] = self.pattern
        return args


class DateTimeSchema(SchemaData):
    _type_string: ClassVar[str] = "datetime"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from datatime import datetime")
        return imports


class DateSchema(SchemaData):
    _type_string: ClassVar[str] = "date"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from datetime import date")
        return imports


class FileSchema(SchemaData):
    _type_string: ClassVar[str] = "FileTypes"

    def get_imports(self) -> Set[str]:
        imports = super().get_imports()
        imports.add("from .types import FileTypes")
        return imports


def build_string_schema(
    source: Source,
) -> Union[StringSchema, DateSchema, DateTimeSchema, FileSchema]:
    data = cast(oas.Schema, source.data)
    if data.schema_format == "date-time":
        return DateTimeSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif data.schema_format == "date":
        return DateSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
        )
    elif data.schema_format == "binary":
        return FileSchema(
            title=data.title,
            description=data.description,
            default=None,
            examples=data.examples or (data.example and [data.example]),
        )
    else:
        return StringSchema(
            title=data.title,
            description=data.description,
            default=data.default,
            examples=data.examples or (data.example and [data.example]),
            min_length=data.minLength,
            max_length=data.maxLength,
            pattern=data.pattern,
        )
