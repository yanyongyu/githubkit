"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict

from .group_0131 import RulesetVersionPropActorType
from .group_0134 import RulesetVersionWithStateAllof1PropStateType


class RulesetVersionWithStateType(TypedDict):
    """RulesetVersionWithState"""

    version_id: int
    actor: RulesetVersionPropActorType
    updated_at: datetime
    state: RulesetVersionWithStateAllof1PropStateType


__all__ = ("RulesetVersionWithStateType",)
