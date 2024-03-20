"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2"""

    labels: Missing[
        List[ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems]
    ] = Field(min_length=1, default=UNSET)


class ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems"""

    name: str = Field()


model_rebuild(ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2)
model_rebuild(ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems)

__all__ = (
    "ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2",
    "ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems",
)