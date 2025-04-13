"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0211 import DeploymentType
from .group_0418 import EnterpriseWebhooksType
from .group_0419 import SimpleInstallationType
from .group_0420 import OrganizationSimpleWebhooksType
from .group_0421 import RepositoryWebhooksType


class WebhookWorkflowJobCompletedType(TypedDict):
    """workflow_job completed event"""

    action: Literal["completed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow_job: WebhookWorkflowJobCompletedPropWorkflowJobType
    deployment: NotRequired[DeploymentType]


class WebhookWorkflowJobCompletedPropWorkflowJobType(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJob"""

    check_run_url: str
    completed_at: str
    conclusion: Literal[
        "success",
        "failure",
        "skipped",
        "cancelled",
        "action_required",
        "neutral",
        "timed_out",
    ]
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: list[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: int
    run_url: str
    runner_group_id: Union[Union[int, None], None]
    runner_group_name: Union[Union[str, None], None]
    runner_id: Union[Union[int, None], None]
    runner_name: Union[Union[str, None], None]
    started_at: str
    status: Literal["queued", "in_progress", "completed", "waiting"]
    head_branch: Union[Union[str, None], None]
    workflow_name: Union[Union[str, None], None]
    steps: list[WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType]
    url: str


class WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps"""

    completed_at: Union[str, None]
    conclusion: Union[None, Literal["failure", "skipped", "success", "cancelled"]]
    name: str
    number: int
    started_at: Union[str, None]
    status: Literal["in_progress", "completed", "queued"]


__all__ = (
    "WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType",
    "WebhookWorkflowJobCompletedPropWorkflowJobType",
    "WebhookWorkflowJobCompletedType",
)
