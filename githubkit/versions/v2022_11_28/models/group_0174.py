"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0075 import Team
from .group_0001 import SimpleUser
from .group_0005 import Integration


class ProtectedBranchPullRequestReviewPropDismissalRestrictions(GitHubModel):
    """ProtectedBranchPullRequestReviewPropDismissalRestrictions"""

    users: Missing[List[SimpleUser]] = Field(
        default=UNSET, description="The list of users with review dismissal access."
    )
    teams: Missing[List[Team]] = Field(
        default=UNSET, description="The list of teams with review dismissal access."
    )
    apps: Missing[List[Integration]] = Field(
        default=UNSET, description="The list of apps with review dismissal access."
    )
    url: Missing[str] = Field(default=UNSET)
    users_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)


class ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances(GitHubModel):
    """ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: Missing[List[SimpleUser]] = Field(
        default=UNSET,
        description="The list of users allowed to bypass pull request requirements.",
    )
    teams: Missing[List[Team]] = Field(
        default=UNSET,
        description="The list of teams allowed to bypass pull request requirements.",
    )
    apps: Missing[List[Integration]] = Field(
        default=UNSET,
        description="The list of apps allowed to bypass pull request requirements.",
    )


model_rebuild(ProtectedBranchPullRequestReviewPropDismissalRestrictions)
model_rebuild(ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances)

__all__ = (
    "ProtectedBranchPullRequestReviewPropDismissalRestrictions",
    "ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances",
)
