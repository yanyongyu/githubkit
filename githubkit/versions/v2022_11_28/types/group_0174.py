"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0075 import TeamType
from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class ProtectedBranchPullRequestReviewPropDismissalRestrictionsType(TypedDict):
    """ProtectedBranchPullRequestReviewPropDismissalRestrictions"""

    users: NotRequired[List[SimpleUserType]]
    teams: NotRequired[List[TeamType]]
    apps: NotRequired[List[IntegrationType]]
    url: NotRequired[str]
    users_url: NotRequired[str]
    teams_url: NotRequired[str]


class ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType(TypedDict):
    """ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: NotRequired[List[SimpleUserType]]
    teams: NotRequired[List[TeamType]]
    apps: NotRequired[List[IntegrationType]]


__all__ = (
    "ProtectedBranchPullRequestReviewPropDismissalRestrictionsType",
    "ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType",
)
