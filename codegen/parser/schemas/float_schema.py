from typing import Dict, ClassVar, Optional, cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import SchemaData


class FloatSchema(SchemaData):
    multiple_of: Optional[float] = None
    maximum: Optional[float] = None
    exclusive_maximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusive_minimum: Optional[float] = None

    _type_string: ClassVar[str] = "float"

    def get_default_args(self) -> Dict[str, str]:
        args = super().get_default_args()
        if self.multiple_of is not None:
            args["multiple_of"] = str(self.multiple_of)
        if self.maximum is not None:
            args["le"] = str(self.maximum)
        if self.exclusive_maximum is not None:
            args["lt"] = str(self.exclusive_maximum)
        if self.minimum is not None:
            args["ge"] = str(self.minimum)
        if self.exclusive_minimum is not None:
            args["gt"] = str(self.exclusive_minimum)
        return args


def build_float_schema(source: Source) -> FloatSchema:
    data = cast(oas.Schema, source.data)
    return FloatSchema(
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
