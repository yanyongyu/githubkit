"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookPageBuild

Event: TypeAlias = WebhookPageBuild

PageBuildEvent: TypeAlias = Event

action_types = WebhookPageBuild

page_build_action_types = action_types

__all__ = ("Event", "PageBuildEvent", "action_types", "page_build_action_types")