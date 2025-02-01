"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0234 import DeploymentType
from .group_0451 import EnterpriseWebhooksType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0454 import RepositoryWebhooksType


class WebhookWorkflowJobInProgressType(TypedDict):
    """workflow_job in_progress event"""

    action: Literal["in_progress"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow_job: WebhookWorkflowJobInProgressPropWorkflowJobType
    deployment: NotRequired[DeploymentType]


class WebhookWorkflowJobInProgressPropWorkflowJobType(TypedDict):
    """WebhookWorkflowJobInProgressPropWorkflowJob"""

    check_run_url: str
    completed_at: Union[Union[str, None], None]
    conclusion: Union[Literal["success", "failure", "cancelled", "neutral"], None]
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
    status: Literal["queued", "in_progress", "completed"]
    head_branch: Union[Union[str, None], None]
    workflow_name: Union[Union[str, None], None]
    steps: list[WebhookWorkflowJobInProgressPropWorkflowJobMergedStepsType]
    url: str


class WebhookWorkflowJobInProgressPropWorkflowJobMergedStepsType(TypedDict):
    """WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps"""

    completed_at: Union[Union[str, None], None]
    conclusion: Union[Literal["failure", "skipped", "success", "cancelled"], None]
    name: str
    number: int
    started_at: Union[Union[str, None], None]
    status: Literal["in_progress", "completed", "queued", "pending"]


__all__ = (
    "WebhookWorkflowJobInProgressPropWorkflowJobMergedStepsType",
    "WebhookWorkflowJobInProgressPropWorkflowJobType",
    "WebhookWorkflowJobInProgressType",
)
