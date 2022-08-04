from typing import Any, Dict, Union

from pydantic import parse_obj_as, parse_raw_as

from githubkit.exception import WebhookTypeNotFound

from .types import WebhookEvent, webhook_event_types


def parse_without_name(payload: Union[str, bytes]) -> WebhookEvent:
    return parse_raw_as(WebhookEvent, payload)


def parse(name: str, payload: Union[str, bytes]) -> WebhookEvent:
    if name not in webhook_event_types:
        raise WebhookTypeNotFound(name)
    return parse_raw_as(webhook_event_types[name], payload)


def parse_obj_without_name(payload: Dict[str, Any]) -> WebhookEvent:
    return parse_obj_as(WebhookEvent, payload)


def parse_obj(name: str, payload: Dict[str, Any]) -> WebhookEvent:
    if name not in webhook_event_types:
        raise WebhookTypeNotFound(name)
    return parse_obj_as(webhook_event_types[name], payload)
