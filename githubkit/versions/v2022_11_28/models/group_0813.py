"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0810 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBase,
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHead,
)


class WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests"""

    base: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropBase = Field()
    head: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItemsPropHead = Field()
    id: float = Field()
    number: float = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests)

__all__ = ("WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests",)
