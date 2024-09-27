"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0029 import TeamType
from .group_0002 import SimpleUserType
from .group_0008 import IntegrationType


class ProtectedBranchPullRequestReviewPropDismissalRestrictionsType(TypedDict):
    """ProtectedBranchPullRequestReviewPropDismissalRestrictions"""

    users: NotRequired[List[SimpleUserType]]
    teams: NotRequired[List[TeamType]]
    apps: NotRequired[List[Union[IntegrationType, None]]]
    url: NotRequired[str]
    users_url: NotRequired[str]
    teams_url: NotRequired[str]


class ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType(TypedDict):
    """ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: NotRequired[List[SimpleUserType]]
    teams: NotRequired[List[TeamType]]
    apps: NotRequired[List[Union[IntegrationType, None]]]


__all__ = (
    "ProtectedBranchPullRequestReviewPropDismissalRestrictionsType",
    "ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType",
)
