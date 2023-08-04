import openapi_pydantic as oas

from ...source import Source
from .schema import BoolSchema
from ..utils import build_boolean


def build_bool_schema(source: Source) -> BoolSchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return BoolSchema(
        title=data.title,
        description=data.description,
        default=build_boolean(data.default)
        if data.default is not None
        else data.default,
        examples=data.examples or (data.example and [data.example]),
    )
