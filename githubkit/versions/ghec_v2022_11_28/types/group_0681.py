"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0454 import ProjectsV2ItemType
from .group_0416 import SimpleInstallationType
from .group_0419 import SimpleUserWebhooksType
from .group_0453 import WebhooksProjectChangesType
from .group_0417 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemRestoredType(TypedDict):
    """Projects v2 Item Restored Event"""

    action: Literal["restored"]
    changes: WebhooksProjectChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ItemRestoredType",)
