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


class ReposOwnerRepoIssuesIssueNumberSubIssuesPostBody(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberSubIssuesPostBody"""

    sub_issue_id: int = Field(
        description="The id of the sub-issue to add. The sub-issue must belong to the same repository owner as the parent issue"
    )
    replace_parent: Missing[bool] = Field(
        default=UNSET,
        description="Option that, when true, instructs the operation to replace the sub-issues current parent issue",
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberSubIssuesPostBody)

__all__ = ("ReposOwnerRepoIssuesIssueNumberSubIssuesPostBody",)
