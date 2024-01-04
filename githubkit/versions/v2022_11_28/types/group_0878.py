"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgInvitationsPostBodyType(TypedDict):
    """OrgsOrgInvitationsPostBody"""

    invitee_id: NotRequired[int]
    email: NotRequired[str]
    role: NotRequired[Literal["admin", "direct_member", "billing_manager", "reinstate"]]
    team_ids: NotRequired[List[int]]


__all__ = ("OrgsOrgInvitationsPostBodyType",)
