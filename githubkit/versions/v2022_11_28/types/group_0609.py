"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookProjectCardConvertedType(TypedDict):
    """project_card converted event"""

    action: Literal["converted"]
    changes: WebhookProjectCardConvertedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhookProjectCardConvertedPropProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookProjectCardConvertedPropChangesType(TypedDict):
    """WebhookProjectCardConvertedPropChanges"""

    note: WebhookProjectCardConvertedPropChangesPropNoteType


class WebhookProjectCardConvertedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardConvertedPropChangesPropNote"""

    from_: str


class WebhookProjectCardConvertedPropProjectCardType(TypedDict):
    """Project Card"""

    after_id: NotRequired[Union[int, None]]
    archived: bool
    column_id: int
    column_url: str
    content_url: NotRequired[str]
    created_at: datetime
    creator: Union[WebhookProjectCardConvertedPropProjectCardPropCreatorType, None]
    id: int
    node_id: str
    note: Union[str, None]
    project_url: str
    updated_at: datetime
    url: str


class WebhookProjectCardConvertedPropProjectCardPropCreatorType(TypedDict):
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
    "WebhookProjectCardConvertedType",
    "WebhookProjectCardConvertedPropChangesType",
    "WebhookProjectCardConvertedPropChangesPropNoteType",
    "WebhookProjectCardConvertedPropProjectCardType",
    "WebhookProjectCardConvertedPropProjectCardPropCreatorType",
)
