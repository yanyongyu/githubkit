"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0413 import ProjectsV2Type
from .group_0379 import SimpleInstallationType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ProjectReopenedType(TypedDict):
    """Projects v2 Project Reopened Event"""

    action: Literal["reopened"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ProjectReopenedType",)
