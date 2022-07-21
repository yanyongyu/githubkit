from typing import Dict, List, Optional

from pydantic import Field, BaseModel

from .parameter import Parameter
from .response import ResponseData
from .request_body import RequestBodyData


class EndpointData(BaseModel):
    path: str
    method: str
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    operation_id: Optional[str] = None
    deprecated: bool = False

    parameters: List[Parameter] = Field(default_factory=list)
    request_body: Optional[RequestBodyData] = None

    success_response: Optional[ResponseData] = None
    error_responses: Dict[str, ResponseData] = Field(default_factory=dict)
