"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoIssuesIssueNumberAssigneesPostBody(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberAssigneesPostBody"""

    assignees: Missing[list[str]] = Field(
        default=UNSET,
        description="Usernames of people to assign this issue to. _NOTE: Only users with push access can add assignees to an issue. Assignees are silently ignored otherwise._",
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberAssigneesPostBody)

__all__ = ("ReposOwnerRepoIssuesIssueNumberAssigneesPostBody",)
