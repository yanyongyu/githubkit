"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType
from .group_0393 import SimpleUserWebhooksType


class WebhookTeamAddType(TypedDict):
    """team_add event"""

    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    team: WebhookTeamAddPropTeamType


class WebhookTeamAddPropTeamType(TypedDict):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[Union[WebhookTeamAddPropTeamPropParentType, None]]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    notification_setting: NotRequired[
        Literal["notifications_enabled", "notifications_disabled"]
    ]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookTeamAddPropTeamPropParentType(TypedDict):
    """WebhookTeamAddPropTeamPropParent"""

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    notification_setting: Literal["notifications_enabled", "notifications_disabled"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookTeamAddType",
    "WebhookTeamAddPropTeamType",
    "WebhookTeamAddPropTeamPropParentType",
)
