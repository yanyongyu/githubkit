"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.utils import TaggedUnion
from githubkit.compat import GitHubModel

from ..models import WebhookPublic

Event: TypeAlias = WebhookPublic

PublicEvent: TypeAlias = Event

action_types = WebhookPublic

public_action_types = action_types

__all__ = ("Event", "PublicEvent", "action_types", "public_action_types")
