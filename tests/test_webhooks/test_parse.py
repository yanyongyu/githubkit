import json
from typing import Any, Dict, List, Type, Tuple
from pathlib import Path

import pytest

from githubkit import GitHub, GitHubModel
from githubkit.versions import LATEST_VERSION
from githubkit.webhooks import (
    parse,
    parse_obj,
    parse_without_name,
    parse_obj_without_name,
)
from githubkit.versions.latest.models import WebhookPush, WebhookPullRequestOpened
from githubkit.versions.latest.webhooks import EventNameType

TEST_CASES: List[Tuple[EventNameType, str, Type[GitHubModel]]] = [
    (
        "push",
        (Path(__file__).parent / "assets/push.json").read_text(encoding="utf-8"),
        WebhookPush,
    ),
    (
        "pull_request",
        (Path(__file__).parent / "assets/pull_request_opened.json").read_text(
            encoding="utf-8"
        ),
        WebhookPullRequestOpened,
    ),
]


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(event_name, payload, event_class, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_parse(event_name: EventNameType, payload: str, event_class: Type[GitHubModel]):
    event = parse(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(payload, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_parse_without_name(payload: str):
    parse_without_name(payload)


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(
            event_name, json.loads(payload), event_class, id=event_class.__name__
        )
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_parse_obj(
    event_name: EventNameType, payload: Dict[str, Any], event_class: Type[GitHubModel]
):
    event = parse_obj(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(json.loads(payload), id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_parse_obj_without_name(payload: Dict[str, Any]):
    parse_obj_without_name(payload)


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(event_name, payload, event_class, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_namespace_parse(
    event_name: EventNameType, payload: str, event_class: Type[GitHubModel]
):
    event = GitHub.webhooks.parse(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(payload, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_namespace_parse_without_name(payload: str):
    GitHub.webhooks.parse_without_name(payload)


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(
            event_name, json.loads(payload), event_class, id=event_class.__name__
        )
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_namespace_parse_obj(
    event_name: EventNameType, payload: Dict[str, Any], event_class: Type[GitHubModel]
):
    event = GitHub.webhooks.parse_obj(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(json.loads(payload), id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_namespace_parse_obj_without_name(payload: Dict[str, Any]):
    GitHub.webhooks.parse_obj_without_name(payload)


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(event_name, payload, event_class, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_versioned_parse(
    event_name: EventNameType, payload: str, event_class: Type[GitHubModel]
):
    event = GitHub.webhooks(LATEST_VERSION).parse(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(payload, id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_versioned_parse_without_name(payload: str):
    GitHub.webhooks(LATEST_VERSION).parse_without_name(payload)


@pytest.mark.parametrize(
    ("event_name", "payload", "event_class"),
    (
        pytest.param(
            event_name, json.loads(payload), event_class, id=event_class.__name__
        )
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_versioned_parse_obj(
    event_name: EventNameType, payload: Dict[str, Any], event_class: Type[GitHubModel]
):
    event = GitHub.webhooks(LATEST_VERSION).parse_obj(event_name, payload)
    assert isinstance(event, event_class), f"event type {type(event)} != {event_class}"


@pytest.mark.parametrize(
    "payload",
    (
        pytest.param(json.loads(payload), id=event_class.__name__)
        for event_name, payload, event_class in TEST_CASES
    ),
)
def test_versioned_parse_obj_without_name(payload: Dict[str, Any]):
    GitHub.webhooks(LATEST_VERSION).parse_obj_without_name(payload)
