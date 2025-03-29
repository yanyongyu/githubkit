"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0417 import EnterpriseWebhooksType
from .group_0418 import SimpleInstallationType
from .group_0419 import OrganizationSimpleWebhooksType
from .group_0420 import RepositoryWebhooksType


class WebhookRepositoryTransferredType(TypedDict):
    """repository transferred event"""

    action: Literal["transferred"]
    changes: WebhookRepositoryTransferredPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryTransferredPropChangesType(TypedDict):
    """WebhookRepositoryTransferredPropChanges"""

    owner: WebhookRepositoryTransferredPropChangesPropOwnerType


class WebhookRepositoryTransferredPropChangesPropOwnerType(TypedDict):
    """WebhookRepositoryTransferredPropChangesPropOwner"""

    from_: WebhookRepositoryTransferredPropChangesPropOwnerPropFromType


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromType(TypedDict):
    """WebhookRepositoryTransferredPropChangesPropOwnerPropFrom"""

    organization: NotRequired[
        WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType
    ]
    user: NotRequired[
        Union[
            WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType, None
        ]
    ]


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType(
    TypedDict
):
    """Organization"""

    avatar_url: str
    description: Union[str, None]
    events_url: str
    hooks_url: str
    html_url: NotRequired[str]
    id: int
    issues_url: str
    login: str
    members_url: str
    node_id: str
    public_members_url: str
    repos_url: str
    url: str


class WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType(TypedDict):
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
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropOrganizationType",
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromPropUserType",
    "WebhookRepositoryTransferredPropChangesPropOwnerPropFromType",
    "WebhookRepositoryTransferredPropChangesPropOwnerType",
    "WebhookRepositoryTransferredPropChangesType",
    "WebhookRepositoryTransferredType",
)
