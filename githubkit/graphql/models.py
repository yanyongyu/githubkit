from typing import Any, Dict, List, Union, Optional

from pydantic import BaseModel, root_validator


class SourceLocation(BaseModel):
    line: int
    column: int


class GraphQLError(BaseModel):
    message: str
    locations: Optional[List[SourceLocation]] = None
    path: Optional[List[Union[int, str]]] = None
    extensions: Optional[Dict[str, Any]] = None


class GraphQLResponse(BaseModel):
    data: Optional[Dict[str, Any]] = None
    errors: Optional[List[GraphQLError]] = None
    extensions: Optional[Dict[str, Any]] = None

    @root_validator
    def validate_data_and_errors(cls, values: Dict[str, Any]):
        if values.get("data") is None and not values.get("errors"):
            raise ValueError("No data or errors found in response")
        return values
