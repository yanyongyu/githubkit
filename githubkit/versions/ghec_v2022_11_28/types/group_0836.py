"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict

from .group_0837 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType,
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType,
)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType
    id: float
    number: float
    url: str


__all__ = ("WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsType",)
