"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0456 import EnterpriseWebhooksType
from .group_0457 import SimpleInstallationType
from .group_0458 import OrganizationSimpleWebhooksType
from .group_0459 import RepositoryWebhooksType
from .group_0469 import WebhooksUserType
from .group_0484 import WebhooksTeamType


class WebhookMembershipRemovedType(TypedDict):
    """membership removed event"""

    action: Literal["removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    member: Union[WebhooksUserType, None]
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    scope: Literal["team", "organization"]
    sender: Union[WebhookMembershipRemovedPropSenderType, None]
    team: WebhooksTeamType


class WebhookMembershipRemovedPropSenderType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookMembershipRemovedPropSenderType",
    "WebhookMembershipRemovedType",
)
