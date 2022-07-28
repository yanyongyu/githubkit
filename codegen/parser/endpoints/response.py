from typing import Set, Union, Optional

import openapi_schema_pydantic as oas
from pydantic import BaseModel, parse_obj_as

from ...source import Source
from ..schemas import SchemaData, parse_schema


class ResponseData(BaseModel):
    description: str
    response_schema: Optional[SchemaData] = None

    def get_using_imports(self) -> Set[str]:
        return (
            self.response_schema.get_using_imports() if self.response_schema else set()
        )


def build_response(source: Source, prefix: str) -> ResponseData:
    data = source.data
    try:
        data = parse_obj_as(Union[oas.Reference, oas.Response], data)
    except Exception as e:
        raise TypeError(f"Invalid Response from {source.uri}") from e

    if isinstance(data, oas.Reference):
        source = source.resolve_ref(data.ref)
        try:
            data = oas.Response.parse_obj(source.data)
        except Exception as e:
            raise TypeError(f"Invalid Response from {source.uri}") from e

    response_schema = None
    if data.content:
        media_type = next(iter(data.content.keys()))
        response_schema = parse_schema(
            source / "content" / media_type / "schema", prefix
        )

    return ResponseData(description=data.description, response_schema=response_schema)
