from typing import TYPE_CHECKING

import openapi_pydantic as oas

from ..data import WebhookData
from ..schemas import parse_schema
from ..utils import concat_snake_name, snake_case, type_ref_from_source

if TYPE_CHECKING:
    from ...source import Source


def parse_webhook(source: "Source") -> WebhookData | None:
    data = source.data
    data = oas.PathItem.model_validate(data)

    operation_source = source / "post"
    operation = data.post
    if not operation:
        return

    webhook_id = operation.operationId
    assert webhook_id is not None, "Webhook operationId is required"
    event: str = webhook_id
    action: str | None = None
    if "/" in webhook_id:
        event, action = webhook_id.split("/")
    # event and action are snake_case
    event = event and snake_case(event)
    action = action and snake_case(action)

    request_body = operation.requestBody
    if not request_body:
        return
    body_source = operation_source / "requestBody"
    while isinstance(request_body, oas.Reference):
        body_source = body_source.resolve_ref(request_body.ref)
        request_body = type_ref_from_source(source, oas.RequestBody)

    # we only consider json body (form data ignored)
    body_schema = parse_schema(
        body_source / "content" / "application/json" / "schema",
        concat_snake_name(event, action) if action else event,
    )

    return WebhookData(event=event, action=action, event_schema=body_schema)
