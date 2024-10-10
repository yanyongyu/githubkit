from typing import Literal
from collections import defaultdict
from dataclasses import field, dataclass

from .schemas import Property, SchemaData, ModelSchema, UnionSchema
from .utils import snake_case, concat_snake_name, fix_reserved_words


@dataclass(eq=False)
class ModelGroup:
    """A group of models that are dependent on each other."""

    models: list[ModelSchema]
    group_dependencies: list["ModelGroup"] = field(default_factory=list)

    @property
    def model_dependencies(self) -> list[ModelSchema]:
        result: list[ModelSchema] = []
        model_ids = {id(model) for model in self.models}
        for model in self.models:
            for dep in model.get_model_dependencies():
                if id(dep) not in model_ids and id(dep) not in set(map(id, result)):
                    result.append(dep)
        return result

    def get_dependency_by_model(self, model: ModelSchema) -> "ModelGroup":
        """Get the group that contains the model."""
        for group in self.group_dependencies:
            # do not use `in` operator to avoid __eq__
            if id(model) in map(id, group.models):
                return group
        raise ValueError(f"Model {model.class_name} not found in any group dependency.")

    def merge_group(self, other: "ModelGroup") -> None:
        """Merge another group into this group."""
        if other in self.group_dependencies:
            self.group_dependencies.remove(other)
        self.models.extend(other.models)
        for group in other.group_dependencies:
            if group not in self.group_dependencies:
                self.group_dependencies.append(group)


@dataclass(kw_only=True)
class Parameter(Property):
    """Parameter data

    This indicates a parameter in the endpoint definition
    with its location, name and schema.
    """

    param_in: Literal["query", "header", "path", "cookie"]


@dataclass(kw_only=True)
class RequestBodyData:
    """Request body data

    This indicates the request body in the endpoint definition
    with its type and schema.
    """

    type: Literal["form", "json", "file", "raw"]
    body_schema: SchemaData
    content_type: str | None = None
    required: bool = False

    @property
    def allowed_models(self) -> list[ModelSchema]:
        if isinstance(self.body_schema, ModelSchema):
            return [self.body_schema]
        elif isinstance(self.body_schema, UnionSchema):
            return [
                schema
                for schema in self.body_schema.schemas
                if isinstance(schema, ModelSchema)
            ]
        return []

    def get_raw_definition(self) -> str:
        prop = Property(
            name="data",
            prop_name="data",
            required=self.required,
            schema_data=self.body_schema,
        )
        return prop.get_param_defination()

    def get_endpoint_definition(self) -> str:
        prop = Property(
            name="data",
            prop_name="data",
            required=not bool(self.allowed_models),
            schema_data=self.body_schema,
        )
        return prop.get_param_defination()


@dataclass(kw_only=True)
class ResponseData:
    """Response data

    This indicates the response data in the endpoint definition
    with its description and schema.
    """

    description: str
    response_schema: SchemaData | None = None


@dataclass(kw_only=True)
class EndpointData:
    path: str
    method: str
    tags: list[str] | None = None
    description: str | None = None
    operation_id: str | None = None
    external_docs: str | None = None
    deprecated: bool = False

    parameters: list[Parameter] = field(default_factory=list)
    request_body: RequestBodyData | None = None

    success_response: ResponseData | None = None
    error_responses: dict[str, ResponseData] = field(default_factory=dict)

    @property
    def category(self) -> str:
        """Separate endpoints by tags"""
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
    def path_params(self) -> list[Parameter]:
        return [param for param in self.parameters if param.param_in == "path"]

    @property
    def query_params(self) -> list[Parameter]:
        return [param for param in self.parameters if param.param_in == "query"]

    @property
    def header_params(self) -> list[Parameter]:
        return [param for param in self.parameters if param.param_in == "header"]

    @property
    def cookie_params(self) -> list[Parameter]:
        return [param for param in self.parameters if param.param_in == "cookie"]

    @property
    def param_names(self) -> list[str]:
        return [param.prop_name for param in self.parameters]


@dataclass
class WebhookData:
    event: str
    action: str | None
    event_schema: SchemaData


@dataclass
class OpenAPIData:
    """All the data needed to generate a client"""

    model_groups: list[ModelGroup]
    endpoints: list[EndpointData]
    webhooks: list[WebhookData]

    @property
    def models(self) -> list[ModelSchema]:
        return [m for g in self.model_groups for m in g.models]

    @property
    def endpoints_by_tag(self) -> dict[str, list[EndpointData]]:
        data: dict[str, list[EndpointData]] = defaultdict(list)
        for endpoint in self.endpoints:
            data[endpoint.category].append(endpoint)
        return data

    @property
    def webhooks_by_event(self) -> dict[str, list[WebhookData]]:
        data: dict[str, list[WebhookData]] = defaultdict(list)
        for webhook in self.webhooks:
            data[webhook.event].append(webhook)
        return data
