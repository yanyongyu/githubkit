"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0428 import SimpleInstallationType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0466 import ProjectsV2StatusUpdateType


class WebhookProjectsV2StatusUpdateCreatedType(TypedDict):
    """Projects v2 Status Update Created Event"""

    action: Literal["created"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_status_update: ProjectsV2StatusUpdateType
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2StatusUpdateCreatedType",)
