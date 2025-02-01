"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0487 import ProjectsV2Type


class WebhookProjectsV2ProjectCreatedType(TypedDict):
    """WebhookProjectsV2ProjectCreated

    A project was created
    """

    action: Literal["created"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2ProjectCreatedType",)
