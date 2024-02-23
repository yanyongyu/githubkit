"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0356 import EnterpriseWebhooksType
from .group_0357 import SimpleInstallationType
from .group_0358 import OrganizationSimpleWebhooksType
from .group_0359 import RepositoryWebhooksType
from .group_0360 import SimpleUserWebhooksType


class WebhookOrganizationMemberRemovedType(TypedDict):
    """organization member_removed event"""

    action: Literal["member_removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    membership: WebhookOrganizationMemberRemovedPropMembershipType
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookOrganizationMemberRemovedPropMembershipType(TypedDict):
    """Membership

    The membership between the user and the organization. Not present when the
    action is `member_invited`.
    """

    organization_url: str
    role: str
    state: str
    url: str
    user: Union[WebhookOrganizationMemberRemovedPropMembershipPropUserType, None]


class WebhookOrganizationMemberRemovedPropMembershipPropUserType(TypedDict):
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


__all__ = (
    "WebhookOrganizationMemberRemovedType",
    "WebhookOrganizationMemberRemovedPropMembershipType",
    "WebhookOrganizationMemberRemovedPropMembershipPropUserType",
)
