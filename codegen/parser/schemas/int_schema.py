from typing import Dict, ClassVar, Optional, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import SchemaData


class IntSchema(SchemaData):
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[float] = None

    _type_string: ClassVar[str] = "int"

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
        if self.multiple_of is not None:
            args["multiple_of"] = repr(self.multiple_of)
        if self.maximum is not None:
            args["le"] = repr(self.maximum)
        if self.exclusive_maximum is not None:
            args["lt"] = repr(self.exclusive_maximum)
        if self.minimum is not None:
            args["ge"] = repr(self.minimum)
        if self.exclusive_minimum is not None:
            args["gt"] = repr(self.exclusive_minimum)
        return args


def build_int_schema(source: Source) -> IntSchema:
    data = cast(oas.Schema, source.data)
    return IntSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        multiple_of=data.multipleOf,
        maximum=data.maximum,
        exclusive_maximum=data.exclusiveMaximum,
        minimum=data.minimum,
        exclusive_minimum=data.exclusiveMinimum,
    )
