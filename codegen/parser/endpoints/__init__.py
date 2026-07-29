from typing import TYPE_CHECKING

import openapi_pydantic as oas

from .. import get_override_config
from ..data import EndpointData as EndpointData
from ..utils import concat_snake_name
from .parameter import build_param
from .request_body import build_request_body
from .response import build_response

if TYPE_CHECKING:
    from ...source import Source


METHODS = ["get", "put", "post", "delete", "options", "head", "patch", "trace"]


def _override_operation_id(
    operation_id: str, operation_overrides: dict[str, str]
) -> str:
    for pattern, override in operation_overrides.items():
        if operation_id.startswith(pattern):
            return override + operation_id.removeprefix(pattern)
    return operation_id


def parse_endpoint(source: "Source", path: str) -> list[EndpointData]:
    data = source.data
    data = oas.PathItem.model_validate(data)

    endpoints: list[EndpointData] = []

    sanitized_path = path.replace("{", "").replace("}", "").replace("/", "_")

    global_params = [
        build_param(
            source / "parameters" / index,
            sanitized_path,
        )
        for index in range(len(data.parameters or []))
    ]

    override_config = get_override_config()
    operation_overrides = override_config.operation_overrides

    for method in METHODS:
        operation_source = source / method
        operation = getattr(data, method, None)
        if not isinstance(operation, oas.Operation):
            continue

        if operation_id := operation.operationId:
            operation_id = _override_operation_id(operation_id, operation_overrides)

        op_params = [
            build_param(
                operation_source / "parameters" / index,
                concat_snake_name(sanitized_path, method),
            )
            for index in range(len(operation.parameters or []))
        ]

        request_body = None
        if operation.requestBody:
            request_body = build_request_body(
                operation_source / "requestBody",
                concat_snake_name(sanitized_path, method),
            )

        responses = {
            code: build_response(
                operation_source / "responses" / code,
                concat_snake_name(sanitized_path, method, "response", code),
            )
            for code in (operation.responses or {}).keys()
        }
        success_response = responses.get(
            next(
                (key for key in responses if key.startswith("2")),
                next((key for key in responses if key.startswith("3")), "default"),
            )
        )
        error_responses = {
            code: response
            for code, response in responses.items()
            if code[-3] not in {"2", "3"}
        }

        endpoints.append(
            EndpointData(
                path=path,
                method=method,
                tags=operation.tags,
                description=operation.description,
                operation_id=operation_id,
                external_docs=operation.externalDocs and operation.externalDocs.url,
                deprecated=operation.deprecated,
                parameters=global_params + op_params,
                request_body=request_body,
                success_response=success_response,
                error_responses=error_responses,
            )
        )

    return endpoints
