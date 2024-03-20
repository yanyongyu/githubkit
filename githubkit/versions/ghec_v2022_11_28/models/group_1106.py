"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof0(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof0"""

    labels: Missing[List[str]] = Field(
        min_length=1,
        default=UNSET,
        description='The names of the labels to add to the issue\'s existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as a `string` or an `array` of labels directly, but GitHub recommends passing an object with the `labels` key. You can also replace all of the labels for an issue. For more information, see "[Set labels for an issue](https://docs.github.com/enterprise-cloud@latest//rest/issues/labels#set-labels-for-an-issue)."',
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof0)

__all__ = ("ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof0",)
