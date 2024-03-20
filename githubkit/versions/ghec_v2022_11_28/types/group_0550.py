"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookIssuesLockedPropIssueAllof1Type(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1"""

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[
        Union[WebhookIssuesLockedPropIssueAllof1PropAssigneeType, None]
    ]
    assignees: NotRequired[
        List[Union[WebhookIssuesLockedPropIssueAllof1PropAssigneesItemsType, None]]
    ]
    author_association: NotRequired[str]
    body: NotRequired[Union[str, None]]
    closed_at: NotRequired[Union[str, None]]
    comments: NotRequired[int]
    comments_url: NotRequired[str]
    created_at: NotRequired[str]
    events_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: NotRequired[
        List[Union[WebhookIssuesLockedPropIssueAllof1PropLabelsItemsType, None]]
    ]
    labels_url: NotRequired[str]
    locked: Literal[True]
    milestone: NotRequired[
        Union[WebhookIssuesLockedPropIssueAllof1PropMilestoneType, None]
    ]
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubAppType, None]
    ]
    reactions: NotRequired[WebhookIssuesLockedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: NotRequired[str]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssuesLockedPropIssueAllof1PropUserType]


class WebhookIssuesLockedPropIssueAllof1PropAssigneeType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropAssignee"""


class WebhookIssuesLockedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesLockedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesLockedPropIssueAllof1PropMilestoneType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropMilestone"""


class WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubAppType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesLockedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropReactions"""

    plus_one: NotRequired[int]
    minus_one: NotRequired[int]
    confused: NotRequired[int]
    eyes: NotRequired[int]
    heart: NotRequired[int]
    hooray: NotRequired[int]
    laugh: NotRequired[int]
    rocket: NotRequired[int]
    total_count: NotRequired[int]
    url: NotRequired[str]


class WebhookIssuesLockedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssuesLockedPropIssueAllof1PropUser"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookIssuesLockedPropIssueAllof1Type",
    "WebhookIssuesLockedPropIssueAllof1PropAssigneeType",
    "WebhookIssuesLockedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssuesLockedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssuesLockedPropIssueAllof1PropMilestoneType",
    "WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubAppType",
    "WebhookIssuesLockedPropIssueAllof1PropReactionsType",
    "WebhookIssuesLockedPropIssueAllof1PropUserType",
)
