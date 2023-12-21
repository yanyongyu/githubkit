from contextvars import ContextVar
from typing import TYPE_CHECKING, Optional

import httpx
from openapi_pydantic import OpenAPI

if TYPE_CHECKING:
    from ..source import Source
    from ..config import Override

# parser context
_override_config: ContextVar["Override"] = ContextVar("override_config")
_schemas: ContextVar[dict[httpx.URL, "SchemaData"]] = ContextVar("schemas")


def get_override_config() -> "Override":
    return _override_config.get()


def get_schemas() -> dict[httpx.URL, "SchemaData"]:
    return _schemas.get()


def get_schema(ref: httpx.URL) -> Optional["SchemaData"]:
    return _schemas.get().get(ref)


def add_schema(ref: httpx.URL, schema: "SchemaData"):
    if ref in _schemas.get():
        raise ValueError(f"Duplicate schema {ref}")
    _schemas.get()[ref] = schema


from .webhooks import parse_webhook
from .endpoints import parse_endpoint
from .utils import sanitize as sanitize
from .utils import kebab_case as kebab_case
from .utils import snake_case as snake_case
from .data import OpenAPIData as OpenAPIData
from .data import WebhookData as WebhookData
from .schemas import SchemaData, parse_schema
from .utils import pascal_case as pascal_case
from .data import EndpointData as EndpointData
from .utils import fix_reserved_words as fix_reserved_words


def parse_openapi_spec(source: "Source", override: "Override") -> OpenAPIData:
    source = source.get_root()

    _ot = _override_config.set(override)
    _st = _schemas.set({})

    try:
        openapi = OpenAPI.model_validate(source.root)

        # pre-cache /components/schemas first
        if openapi.components and openapi.components.schemas:
            schemas_source = source / "components" / "schemas"
            for name in openapi.components.schemas:
                schema_source = schemas_source / name
                parse_schema(schema_source, name)

        # load endpoints
        endpoints: list[EndpointData] = []
        if openapi.paths:
            for path in openapi.paths:
                endpoints.extend(parse_endpoint(source / "paths" / path, path))

        # load webhooks
        webhooks: list[WebhookData] = []
        if openapi.webhooks:
            for webhook in openapi.webhooks:
                if webhook_data := parse_webhook(source / "webhooks" / webhook):
                    webhooks.append(webhook_data)

        return OpenAPIData(
            schemas=list(get_schemas().values()), endpoints=endpoints, webhooks=webhooks
        )
    finally:
        _override_config.reset(_ot)
        _schemas.reset(_st)
