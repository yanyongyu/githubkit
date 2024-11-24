"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0386 import SimpleInstallationType
from .group_0387 import OrganizationSimpleWebhooksType
from .group_0421 import ProjectsV2ItemType


class WebhookProjectsV2ItemReorderedType(TypedDict):
    """Projects v2 Item Reordered Event"""

    action: Literal["reordered"]
    changes: WebhookProjectsV2ItemReorderedPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserType


class WebhookProjectsV2ItemReorderedPropChangesType(TypedDict):
    """WebhookProjectsV2ItemReorderedPropChanges"""

    previous_projects_v2_item_node_id: NotRequired[
        WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeIdType
    ]


class WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeIdType(
    TypedDict
):
    """WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


__all__ = (
    "WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeIdType",
    "WebhookProjectsV2ItemReorderedPropChangesType",
    "WebhookProjectsV2ItemReorderedType",
)
