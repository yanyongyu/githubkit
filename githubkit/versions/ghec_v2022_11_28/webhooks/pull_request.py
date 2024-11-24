"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel
from githubkit.utils import TaggedUnion

from ..models import (
    WebhookPullRequestAssigned,
    WebhookPullRequestAutoMergeDisabled,
    WebhookPullRequestAutoMergeEnabled,
    WebhookPullRequestClosed,
    WebhookPullRequestConvertedToDraft,
    WebhookPullRequestDemilestoned,
    WebhookPullRequestDequeued,
    WebhookPullRequestEdited,
    WebhookPullRequestEnqueued,
    WebhookPullRequestLabeled,
    WebhookPullRequestLocked,
    WebhookPullRequestMilestoned,
    WebhookPullRequestOpened,
    WebhookPullRequestReadyForReview,
    WebhookPullRequestReopened,
    WebhookPullRequestReviewRequestedOneof0,
    WebhookPullRequestReviewRequestedOneof1,
    WebhookPullRequestReviewRequestRemovedOneof0,
    WebhookPullRequestReviewRequestRemovedOneof1,
    WebhookPullRequestSynchronize,
    WebhookPullRequestUnassigned,
    WebhookPullRequestUnlabeled,
    WebhookPullRequestUnlocked,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookPullRequestAssigned,
        WebhookPullRequestAutoMergeDisabled,
        WebhookPullRequestAutoMergeEnabled,
        WebhookPullRequestClosed,
        WebhookPullRequestConvertedToDraft,
        WebhookPullRequestDemilestoned,
        WebhookPullRequestDequeued,
        WebhookPullRequestEdited,
        WebhookPullRequestEnqueued,
        WebhookPullRequestLabeled,
        WebhookPullRequestLocked,
        WebhookPullRequestMilestoned,
        WebhookPullRequestOpened,
        WebhookPullRequestReadyForReview,
        WebhookPullRequestReopened,
        Annotated[
            Union[
                WebhookPullRequestReviewRequestRemovedOneof0,
                WebhookPullRequestReviewRequestRemovedOneof1,
            ],
            TaggedUnion(
                Union[
                    WebhookPullRequestReviewRequestRemovedOneof0,
                    WebhookPullRequestReviewRequestRemovedOneof1,
                ],
                "action",
                "review_request_removed",
            ),
        ],
        Annotated[
            Union[
                WebhookPullRequestReviewRequestedOneof0,
                WebhookPullRequestReviewRequestedOneof1,
            ],
            TaggedUnion(
                Union[
                    WebhookPullRequestReviewRequestedOneof0,
                    WebhookPullRequestReviewRequestedOneof1,
                ],
                "action",
                "review_requested",
            ),
        ],
        WebhookPullRequestSynchronize,
        WebhookPullRequestUnassigned,
        WebhookPullRequestUnlabeled,
        WebhookPullRequestUnlocked,
    ],
    Field(discriminator="action"),
]

PullRequestEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "assigned": WebhookPullRequestAssigned,
    "auto_merge_disabled": WebhookPullRequestAutoMergeDisabled,
    "auto_merge_enabled": WebhookPullRequestAutoMergeEnabled,
    "closed": WebhookPullRequestClosed,
    "converted_to_draft": WebhookPullRequestConvertedToDraft,
    "demilestoned": WebhookPullRequestDemilestoned,
    "dequeued": WebhookPullRequestDequeued,
    "edited": WebhookPullRequestEdited,
    "enqueued": WebhookPullRequestEnqueued,
    "labeled": WebhookPullRequestLabeled,
    "locked": WebhookPullRequestLocked,
    "milestoned": WebhookPullRequestMilestoned,
    "opened": WebhookPullRequestOpened,
    "ready_for_review": WebhookPullRequestReadyForReview,
    "reopened": WebhookPullRequestReopened,
    "review_request_removed": Union[
        WebhookPullRequestReviewRequestRemovedOneof0,
        WebhookPullRequestReviewRequestRemovedOneof1,
    ],
    "review_requested": Union[
        WebhookPullRequestReviewRequestedOneof0, WebhookPullRequestReviewRequestedOneof1
    ],
    "synchronize": WebhookPullRequestSynchronize,
    "unassigned": WebhookPullRequestUnassigned,
    "unlabeled": WebhookPullRequestUnlabeled,
    "unlocked": WebhookPullRequestUnlocked,
}

pull_request_action_types = action_types

__all__ = ("Event", "PullRequestEvent", "action_types", "pull_request_action_types")
