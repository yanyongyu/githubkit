"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class TeamsTeamIdPatchBodyType(TypedDict):
    """TeamsTeamIdPatchBody"""

    name: str
    description: NotRequired[str]
    privacy: NotRequired[Literal["secret", "closed"]]
    notification_setting: NotRequired[
        Literal["notifications_enabled", "notifications_disabled"]
    ]
    permission: NotRequired[Literal["pull", "push", "admin"]]
    parent_team_id: NotRequired[Union[int, None]]


__all__ = ("TeamsTeamIdPatchBodyType",)
