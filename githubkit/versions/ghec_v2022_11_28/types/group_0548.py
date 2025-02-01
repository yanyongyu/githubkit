"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0234 import DeploymentType
from .group_0365 import PullRequestType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0454 import RepositoryWebhooksType


class WebhookDeploymentProtectionRuleRequestedType(TypedDict):
    """deployment protection rule requested event"""

    action: Literal["requested"]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[DeploymentType]
    pull_requests: NotRequired[list[PullRequestType]]
    repository: NotRequired[RepositoryWebhooksType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookDeploymentProtectionRuleRequestedType",)
