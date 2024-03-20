"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias


from ..models import WebhookRepositoryDispatchSample

Event: TypeAlias = WebhookRepositoryDispatchSample

RepositoryDispatchEvent: TypeAlias = Event

action_types = WebhookRepositoryDispatchSample

repository_dispatch_action_types = action_types

__all__ = (
    "Event",
    "RepositoryDispatchEvent",
    "action_types",
    "repository_dispatch_action_types",
)
