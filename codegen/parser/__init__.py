from contextvars import ContextVar
from typing import Dict, List, Tuple, Union, Optional

import httpx
from openapi_pydantic import OpenAPI

# parser context
_override_config: ContextVar[Tuple["Overridable", ...]] = ContextVar("override_config")
_schemas: ContextVar[Dict[httpx.URL, "SchemaData"]] = ContextVar("schemas")


def get_override_config() -> Tuple["Overridable", ...]:
    return _override_config.get()


def get_schemas() -> Dict[httpx.URL, "SchemaData"]:
    return _schemas.get()


def get_schema(ref: httpx.URL) -> Optional["SchemaData"]:
    return _schemas.get().get(ref)


def add_schema(ref: httpx.URL, schema: "SchemaData"):
    if ref in _schemas.get():
        raise ValueError(f"Duplicate schema {ref}")
    _schemas.get()[ref] = schema


from ..source import Source
from .utils import merge_dict
from .endpoints import parse_endpoint
from .utils import sanitize as sanitize
from .utils import kebab_case as kebab_case
from .utils import snake_case as snake_case
from .data import OpenAPIData as OpenAPIData
from .data import WebhookData as WebhookData
from .utils import pascal_case as pascal_case
from .endpoints import EndpointData as EndpointData
from .schemas import SchemaData, UnionSchema, parse_schema
from .utils import fix_reserved_words as fix_reserved_words
from ..config import Config, RestConfig, Overridable, WebhookConfig


def parse_openapi_spec(source: Source, rest: RestConfig, config: Config) -> OpenAPIData:
    source = source.get_root()

    # apply schema overrides first
    for path, new_schema in {
        **config.schema_overrides,
        **rest.schema_overrides,
    }.items():
        ref = str(httpx.URL(fragment=path))
        merge_dict(source.resolve_ref(ref).data, new_schema)

    _ot = _override_config.set((rest, config))
    _st = _schemas.set({})

    try:
        openapi = OpenAPI.model_validate(source.root)

        # cache /components/schemas first
        if openapi.components and openapi.components.schemas:
            schemas_source = source / "components" / "schemas"
            for name in openapi.components.schemas:
                schema_source = schemas_source / name
                parse_schema(schema_source, name)

        endpoints: List[EndpointData] = []
        if openapi.paths:
            for path in openapi.paths:
                endpoints.extend(parse_endpoint(source / "paths" / path, path))

        return OpenAPIData(
            title=openapi.info.title,
            description=openapi.info.description,
            version=openapi.info.version,
            endpoints=endpoints,
            schemas=list(get_schemas().values()),
        )
    finally:
        _override_config.reset(_ot)
        _schemas.reset(_st)


def parse_webhook_schema(
    source: Source, webhook: WebhookConfig, config: Config
) -> WebhookData:
    source = source.get_root()

    # apply schema overrides first
    for path, new_schema in {
        **config.schema_overrides,
        **webhook.schema_overrides,
    }.items():
        ref = str(httpx.URL(fragment=path))
        merge_dict(source.resolve_ref(ref).data, new_schema)

    _ot = _override_config.set((webhook, config))
    _st = _schemas.set({})

    try:
        root_schema = parse_schema(source, "webhook_schema")
        if not isinstance(root_schema, UnionSchema):
            raise TypeError("Webhook root schema must be a UnionSchema")

        schemas = get_schemas()
        definitions: Dict[str, Union[SchemaData, Dict[str, SchemaData]]] = {}
        for event in source.data["oneOf"]:
            event_name = event["$ref"].split("/")[-1]
            event_source = source.resolve_ref(event["$ref"])
            schema = schemas[event_source.uri]
            if isinstance(schema, UnionSchema):
                definitions[event_name] = {
                    action["$ref"].split("/")[-1]: schemas[
                        event_source.resolve_ref(action["$ref"]).uri
                    ]
                    for action in event_source.data["oneOf"]
                }
            else:
                definitions[event_name] = schema

        return WebhookData(
            schemas=list(schemas.values()),
            definitions=definitions,
        )
    finally:
        _override_config.reset(_ot)
        _schemas.reset(_st)
