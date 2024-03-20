"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0803 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase,
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead,
)


class WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequests(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequests"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase = Field()
    head: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead = Field()
    id: float = Field()
    number: float = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequests)

__all__ = ("WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequests",)
