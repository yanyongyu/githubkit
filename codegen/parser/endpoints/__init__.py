from typing import List

import openapi_schema_pydantic as oas

from ...source import Source
from .parameter import build_param
from .response import build_response
from ..utils import concat_snake_name
from .request_body import build_request_body
from .endpoint import EndpointData as EndpointData

METHODS = ["get", "put", "post", "delete", "options", "head", "patch", "trace"]


def parse_endpoint(source: Source, path: str) -> List[EndpointData]:
    data = source.data
    data = oas.PathItem.parse_obj(data)

    endpoints: List[EndpointData] = []

    sanitized_path = path.replace("{", "").replace("}", "").replace("/", "_")

    global_params = [
        build_param(
            source / "parameters" / index,
            sanitized_path,
        )
        for index in range(len(data.parameters or []))
    ]

    for method in METHODS:
        operation_source = source / method
        operation = getattr(data, method)
        if not isinstance(operation, oas.Operation):
            continue

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
                operation_id=operation.operationId,
                deprecated=operation.deprecated,
                parameters=global_params + op_params,
                request_body=request_body,
                success_response=success_response,
                error_responses=error_responses,
            )
        )

    return endpoints
