"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookDiscussionCreatedType(TypedDict):
    """discussion created event"""

    action: Literal["created"]
    discussion: WebhookDiscussionCreatedPropDiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDiscussionCreatedPropDiscussionType(TypedDict):
    """WebhookDiscussionCreatedPropDiscussion"""

    active_lock_reason: Union[None, None]
    answer_chosen_at: Union[None, None]
    answer_chosen_by: Union[None, None]
    answer_html_url: Union[Union[str, None], None]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: Union[Union[str, None], None]
    category: WebhookDiscussionCreatedPropDiscussionMergedCategoryType
    comments: int
    created_at: datetime
    html_url: str
    id: int
    locked: Literal[False]
    node_id: str
    number: int
    reactions: NotRequired[WebhookDiscussionCreatedPropDiscussionMergedReactionsType]
    repository_url: str
    state: Literal["open", "converting", "transferring"]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    user: WebhookDiscussionCreatedPropDiscussionMergedUserType


class WebhookDiscussionCreatedPropDiscussionMergedCategoryType(TypedDict):
    """WebhookDiscussionCreatedPropDiscussionMergedCategory"""

    created_at: datetime
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: NotRequired[str]
    repository_id: int
    slug: str
    updated_at: str


class WebhookDiscussionCreatedPropDiscussionMergedReactionsType(TypedDict):
    """WebhookDiscussionCreatedPropDiscussionMergedReactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookDiscussionCreatedPropDiscussionMergedUserType(TypedDict):
    """WebhookDiscussionCreatedPropDiscussionMergedUser"""

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
    "WebhookDiscussionCreatedType",
    "WebhookDiscussionCreatedPropDiscussionType",
    "WebhookDiscussionCreatedPropDiscussionMergedCategoryType",
    "WebhookDiscussionCreatedPropDiscussionMergedReactionsType",
    "WebhookDiscussionCreatedPropDiscussionMergedUserType",
)
