"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0359 import OrganizationSimpleWebhooksType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0808 import WebhookWorkflowRunInProgressPropWorkflowRunType


class WebhookWorkflowRunInProgressType(TypedDict):
    """workflow_run in_progress event"""

    action: Literal["in_progress"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow: Union[WebhookWorkflowRunInProgressPropWorkflowType, None]
    workflow_run: WebhookWorkflowRunInProgressPropWorkflowRunType


class WebhookWorkflowRunInProgressPropWorkflowType(TypedDict):
    """Workflow"""

    badge_url: str
    created_at: datetime
    html_url: str
    id: int
    name: str
    node_id: str
    path: str
    state: str
    updated_at: datetime
    url: str


__all__ = (
    "WebhookWorkflowRunInProgressType",
    "WebhookWorkflowRunInProgressPropWorkflowType",
)
