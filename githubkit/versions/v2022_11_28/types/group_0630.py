"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0413 import ProjectsV2Type
from .group_0379 import SimpleInstallationType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ProjectEditedType(TypedDict):
    """Projects v2 Project Edited Event"""

    action: Literal["edited"]
    changes: WebhookProjectsV2ProjectEditedPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserWebhooksType


class WebhookProjectsV2ProjectEditedPropChangesType(TypedDict):
    """WebhookProjectsV2ProjectEditedPropChanges"""

    description: NotRequired[
        WebhookProjectsV2ProjectEditedPropChangesPropDescriptionType
    ]
    public: NotRequired[WebhookProjectsV2ProjectEditedPropChangesPropPublicType]
    short_description: NotRequired[
        WebhookProjectsV2ProjectEditedPropChangesPropShortDescriptionType
    ]
    title: NotRequired[WebhookProjectsV2ProjectEditedPropChangesPropTitleType]


class WebhookProjectsV2ProjectEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookProjectsV2ProjectEditedPropChangesPropDescription"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


class WebhookProjectsV2ProjectEditedPropChangesPropPublicType(TypedDict):
    """WebhookProjectsV2ProjectEditedPropChangesPropPublic"""

    from_: NotRequired[bool]
    to: NotRequired[bool]


class WebhookProjectsV2ProjectEditedPropChangesPropShortDescriptionType(TypedDict):
    """WebhookProjectsV2ProjectEditedPropChangesPropShortDescription"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


class WebhookProjectsV2ProjectEditedPropChangesPropTitleType(TypedDict):
    """WebhookProjectsV2ProjectEditedPropChangesPropTitle"""

    from_: NotRequired[str]
    to: NotRequired[str]


__all__ = (
    "WebhookProjectsV2ProjectEditedType",
    "WebhookProjectsV2ProjectEditedPropChangesType",
    "WebhookProjectsV2ProjectEditedPropChangesPropDescriptionType",
    "WebhookProjectsV2ProjectEditedPropChangesPropPublicType",
    "WebhookProjectsV2ProjectEditedPropChangesPropShortDescriptionType",
    "WebhookProjectsV2ProjectEditedPropChangesPropTitleType",
)
