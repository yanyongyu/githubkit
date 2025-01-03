"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrgsOrgTeamsPostBodyType(TypedDict):
    """OrgsOrgTeamsPostBody"""

    name: str
    description: NotRequired[str]
    maintainers: NotRequired[list[str]]
    repo_names: NotRequired[list[str]]
    privacy: NotRequired[Literal["secret", "closed"]]
    notification_setting: NotRequired[
        Literal["notifications_enabled", "notifications_disabled"]
    ]
    permission: NotRequired[Literal["pull", "push"]]
    parent_team_id: NotRequired[int]


__all__ = ("OrgsOrgTeamsPostBodyType",)
