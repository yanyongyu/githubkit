from typing import Any, Dict, AnyStr

from pydantic import parse_obj_as, parse_raw_as

from githubkit.exception import WebhookTypeNotFound

from .models import WebhookEvent, webhook_events


def parse_without_name(payload: AnyStr) -> WebhookEvent:
    return parse_raw_as(WebhookEvent, payload)


def parse(name: str, payload: AnyStr) -> WebhookEvent:
    if name not in webhook_events:
        raise WebhookTypeNotFound(name)
    return parse_raw_as(webhook_events[name], payload)


def parse_obj_without_name(payload: Dict[str, Any]) -> WebhookEvent:
    return parse_obj_as(WebhookEvent, payload)


def parse_obj(name: str, payload: Dict[str, Any]) -> WebhookEvent:
    if name not in webhook_events:
        raise WebhookTypeNotFound(name)
    return parse_obj_as(webhook_events[name], payload)
