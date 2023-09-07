from typing import Any, Dict, Union

from pydantic import TypeAdapter

from githubkit.exception import WebhookTypeNotFound

from .types import WebhookEvent, webhook_event_types


def parse_without_name(payload: Union[str, bytes]) -> WebhookEvent:
    return TypeAdapter(WebhookEvent).validate_json(payload)


def parse(name: str, payload: Union[str, bytes]) -> WebhookEvent:
    if name not in webhook_event_types:
        raise WebhookTypeNotFound(name)
    return TypeAdapter(webhook_event_types[name]).validate_json(payload)


def parse_obj_without_name(payload: Dict[str, Any]) -> WebhookEvent:
    return TypeAdapter(WebhookEvent).validate_python(payload)


def parse_obj(name: str, payload: Dict[str, Any]) -> WebhookEvent:
    if name not in webhook_event_types:
        raise WebhookTypeNotFound(name)
    return TypeAdapter(webhook_event_types[name]).validate_python(payload)
