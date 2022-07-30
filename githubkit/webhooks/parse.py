from typing import AnyStr

from pydantic import parse_obj_as

from githubkit.exception import WebhookTypeNotFound

from .models import WebhookEvent, webhook_events


def parse_without_name(payload: AnyStr) -> WebhookEvent:
    return parse_obj_as(WebhookEvent, payload)


def parse(name: str, payload: AnyStr) -> WebhookEvent:
    if name not in webhook_events:
        raise WebhookTypeNotFound(name)
    return parse_obj_as(webhook_events[name], payload)
