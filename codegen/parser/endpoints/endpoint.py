from typing import Set, Dict, List, Optional

from pydantic import Field, BaseModel

from .parameter import Parameter
from .response import ResponseData
from .request_body import RequestBodyData
from ..utils import snake_case, concat_snake_name, fix_reserved_words


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

    @property
    def category(self) -> str:
        return fix_reserved_words(snake_case(self.tags[0])) if self.tags else "default"

    @property
    def name(self) -> str:
        if self.operation_id:
            if "/" in self.operation_id:
                return snake_case(self.operation_id.split("/")[-1])
            return snake_case(self.operation_id)
        return concat_snake_name(
            self.method, self.path.replace("{", "").replace("}", "").replace("/", "_")
        )

    @property
    def path_params(self) -> List[Parameter]:
        return [param for param in self.parameters if param.param_in == "path"]

    @property
    def query_params(self) -> List[Parameter]:
        return [param for param in self.parameters if param.param_in == "query"]

    @property
    def header_params(self) -> List[Parameter]:
        return [param for param in self.parameters if param.param_in == "header"]

    @property
    def cookie_params(self) -> List[Parameter]:
        return [param for param in self.parameters if param.param_in == "cookie"]

    @property
    def param_names(self) -> List[str]:
        return [param.prop_name for param in self.parameters]

    def get_imports(self) -> Set[str]:
        imports = set()
        for param in self.parameters:
            imports.update(param.get_param_imports())
        if self.request_body:
            imports.update(self.request_body.get_param_imports())
            imports.update(self.request_body.get_using_imports())
            if self.request_body.allowed_models:
                imports.add("from githubkit.utils import UNSET, Missing")
        if self.success_response:
            imports.update(self.success_response.get_using_imports())
        for resp in self.error_responses.values():
            imports.update(resp.get_using_imports())
        return imports
