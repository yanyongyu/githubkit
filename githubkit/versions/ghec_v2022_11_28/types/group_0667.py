"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0393 import SimpleUserWebhooksType
from .group_0400 import ProjectsV2ItemType


class WebhookProjectsV2ItemRestoredType(TypedDict):
    """Projects v2 Item Restored Event"""

    action: Literal["restored"]
    changes: WebhookProjectsV2ItemRestoredPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


class WebhookProjectsV2ItemRestoredPropChangesType(TypedDict):
    """WebhookProjectsV2ItemRestoredPropChanges"""

    archived_at: NotRequired[WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType]


class WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType(TypedDict):
    """WebhookProjectsV2ItemRestoredPropChangesPropArchivedAt"""

    from_: NotRequired[Union[datetime, None]]
    to: NotRequired[Union[datetime, None]]


__all__ = (
    "WebhookProjectsV2ItemRestoredType",
    "WebhookProjectsV2ItemRestoredPropChangesType",
    "WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType",
)
