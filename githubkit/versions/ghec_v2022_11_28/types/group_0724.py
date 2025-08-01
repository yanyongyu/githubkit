"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0487 import EnterpriseWebhooksType
from .group_0488 import SimpleInstallationType
from .group_0489 import OrganizationSimpleWebhooksType
from .group_0490 import RepositoryWebhooksType
from .group_0500 import WebhooksUserType


class WebhookOrganizationMemberInvitedType(TypedDict):
    """organization member_invited event"""

    action: Literal["member_invited"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    invitation: WebhookOrganizationMemberInvitedPropInvitationType
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType
    user: NotRequired[Union[WebhooksUserType, None]]


class WebhookOrganizationMemberInvitedPropInvitationType(TypedDict):
    """WebhookOrganizationMemberInvitedPropInvitation

    The invitation for the user or email if the action is `member_invited`.
    """

    created_at: datetime
    email: Union[str, None]
    failed_at: Union[datetime, None]
    failed_reason: Union[str, None]
    id: float
    invitation_teams_url: str
    inviter: Union[WebhookOrganizationMemberInvitedPropInvitationPropInviterType, None]
    login: Union[str, None]
    node_id: str
    role: str
    team_count: float
    invitation_source: NotRequired[str]


class WebhookOrganizationMemberInvitedPropInvitationPropInviterType(TypedDict):
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
    "WebhookOrganizationMemberInvitedPropInvitationPropInviterType",
    "WebhookOrganizationMemberInvitedPropInvitationType",
    "WebhookOrganizationMemberInvitedType",
)
