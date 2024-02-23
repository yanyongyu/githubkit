"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ReposOwnerRepoIssuesPostBody(GitHubModel):
    """ReposOwnerRepoIssuesPostBody"""

    title: Union[str, int] = Field(description="The title of the issue.")
    body: Missing[str] = Field(default=UNSET, description="The contents of the issue.")
    assignee: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Login for the user that this issue should be assigned to. _NOTE: Only users with push access can set the assignee for new issues. The assignee is silently dropped otherwise. **This field is deprecated.**_",
    )
    milestone: Missing[Union[str, int, None]] = Field(default=UNSET)
    labels: Missing[
        List[Union[str, ReposOwnerRepoIssuesPostBodyPropLabelsItemsOneof1]]
    ] = Field(
        default=UNSET,
        description="Labels to associate with this issue. _NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise._",
    )
    assignees: Missing[List[str]] = Field(
        default=UNSET,
        description="Logins for Users to assign to this issue. _NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise._",
    )


class ReposOwnerRepoIssuesPostBodyPropLabelsItemsOneof1(GitHubModel):
    """ReposOwnerRepoIssuesPostBodyPropLabelsItemsOneof1"""

    id: Missing[int] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)
    color: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(ReposOwnerRepoIssuesPostBody)
model_rebuild(ReposOwnerRepoIssuesPostBodyPropLabelsItemsOneof1)

__all__ = (
    "ReposOwnerRepoIssuesPostBody",
    "ReposOwnerRepoIssuesPostBodyPropLabelsItemsOneof1",
)
