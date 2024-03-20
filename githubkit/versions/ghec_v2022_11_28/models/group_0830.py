"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0187 import Deployment
from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0392 import OrganizationSimpleWebhooks
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks


class WebhookWorkflowJobQueued(GitHubModel):
    """workflow_job queued event"""

    action: Literal["queued"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    workflow_job: WebhookWorkflowJobQueuedPropWorkflowJob = Field()
    deployment: Missing[Deployment] = Field(
        default=UNSET,
        title="Deployment",
        description="A request for a specific ref(branch,sha,tag) to be deployed",
    )


class WebhookWorkflowJobQueuedPropWorkflowJob(GitHubModel):
    """WebhookWorkflowJobQueuedPropWorkflowJob"""

    check_run_url: str = Field()
    completed_at: Union[str, None] = Field()
    conclusion: Union[str, None] = Field()
    created_at: str = Field(description="The time that the job created.")
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: List[str] = Field()
    name: str = Field()
    node_id: str = Field()
    run_attempt: int = Field()
    run_id: int = Field()
    run_url: str = Field()
    runner_group_id: Union[int, None] = Field()
    runner_group_name: Union[str, None] = Field()
    runner_id: Union[int, None] = Field()
    runner_name: Union[str, None] = Field()
    started_at: datetime = Field()
    status: Literal["queued", "in_progress", "completed", "waiting"] = Field()
    head_branch: Union[str, None] = Field(description="The name of the current branch.")
    workflow_name: Union[str, None] = Field(description="The name of the workflow.")
    steps: List[WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItems] = Field()
    url: str = Field()


class WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItems(GitHubModel):
    """Workflow Step"""

    completed_at: Union[str, None] = Field()
    conclusion: Union[
        None, Literal["failure", "skipped", "success", "cancelled"]
    ] = Field()
    name: str = Field()
    number: int = Field()
    started_at: Union[str, None] = Field()
    status: Literal["completed", "in_progress", "queued", "pending"] = Field()


model_rebuild(WebhookWorkflowJobQueued)
model_rebuild(WebhookWorkflowJobQueuedPropWorkflowJob)
model_rebuild(WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItems)

__all__ = (
    "WebhookWorkflowJobQueued",
    "WebhookWorkflowJobQueuedPropWorkflowJob",
    "WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItems",
)
