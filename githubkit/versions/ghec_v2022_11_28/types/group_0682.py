"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0428 import SimpleInstallationType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0463 import ProjectsV2Type


class WebhookProjectsV2ProjectClosedType(TypedDict):
    """Projects v2 Project Closed Event"""

    action: Literal["closed"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2ProjectClosedType",)
