"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookDeploymentCreated

Event: TypeAlias = WebhookDeploymentCreated

DeploymentEvent: TypeAlias = Event

action_types = WebhookDeploymentCreated

deployment_action_types = action_types

__all__ = ("DeploymentEvent", "Event", "action_types", "deployment_action_types")
