"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookIssueCommentDeletedPropIssueAllof1(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1"""

    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Union[WebhookIssueCommentDeletedPropIssueAllof1PropAssignee, None] = (
        Field(title="User")
    )
    assignees: Missing[
        List[Union[WebhookIssueCommentDeletedPropIssueAllof1PropAssigneesItems, None]]
    ] = Field(default=UNSET)
    author_association: Missing[str] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(default=UNSET)
    closed_at: Missing[Union[str, None]] = Field(default=UNSET)
    comments: Missing[int] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: List[WebhookIssueCommentDeletedPropIssueAllof1PropLabelsItems] = Field()
    labels_url: Missing[str] = Field(default=UNSET)
    locked: bool = Field()
    milestone: Missing[
        Union[WebhookIssueCommentDeletedPropIssueAllof1PropMilestone, None]
    ] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssueCommentDeletedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssueCommentDeletedPropIssueAllof1PropReactions] = Field(
        default=UNSET
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Literal["open", "closed"] = Field(
        description="State of the issue; either 'open' or 'closed'"
    )
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookIssueCommentDeletedPropIssueAllof1PropUser] = Field(
        default=UNSET
    )


class WebhookIssueCommentDeletedPropIssueAllof1PropAssignee(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentDeletedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1PropAssigneesItems"""


class WebhookIssueCommentDeletedPropIssueAllof1PropLabelsItems(GitHubModel):
    """Label"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssueCommentDeletedPropIssueAllof1PropMilestone(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1PropMilestone"""


class WebhookIssueCommentDeletedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssueCommentDeletedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1PropReactions"""

    plus_one: Missing[int] = Field(default=UNSET, alias="+1")
    minus_one: Missing[int] = Field(default=UNSET, alias="-1")
    confused: Missing[int] = Field(default=UNSET)
    eyes: Missing[int] = Field(default=UNSET)
    heart: Missing[int] = Field(default=UNSET)
    hooray: Missing[int] = Field(default=UNSET)
    laugh: Missing[int] = Field(default=UNSET)
    rocket: Missing[int] = Field(default=UNSET)
    total_count: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentDeletedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueAllof1PropUser"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssueCommentDeletedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssueCommentDeletedPropIssueAllof1",
    "WebhookIssueCommentDeletedPropIssueAllof1PropAssignee",
    "WebhookIssueCommentDeletedPropIssueAllof1PropAssigneesItems",
    "WebhookIssueCommentDeletedPropIssueAllof1PropLabelsItems",
    "WebhookIssueCommentDeletedPropIssueAllof1PropMilestone",
    "WebhookIssueCommentDeletedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssueCommentDeletedPropIssueAllof1PropReactions",
    "WebhookIssueCommentDeletedPropIssueAllof1PropUser",
)
