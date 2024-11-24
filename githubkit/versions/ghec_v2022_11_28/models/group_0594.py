"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class WebhookIssueCommentEditedPropIssueAllof1(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1"""

    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Union[WebhookIssueCommentEditedPropIssueAllof1PropAssignee, None] = Field(
        title="User"
    )
    assignees: Missing[
        list[Union[WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems, None]]
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
    labels: list[WebhookIssueCommentEditedPropIssueAllof1PropLabelsItems] = Field()
    labels_url: Missing[str] = Field(default=UNSET)
    locked: bool = Field()
    milestone: Missing[
        Union[WebhookIssueCommentEditedPropIssueAllof1PropMilestone, None]
    ] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssueCommentEditedPropIssueAllof1PropReactions] = Field(
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
    user: Missing[WebhookIssueCommentEditedPropIssueAllof1PropUser] = Field(
        default=UNSET
    )


class WebhookIssueCommentEditedPropIssueAllof1PropAssignee(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems"""


class WebhookIssueCommentEditedPropIssueAllof1PropLabelsItems(GitHubModel):
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


class WebhookIssueCommentEditedPropIssueAllof1PropMilestone(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1PropMilestone"""


class WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssueCommentEditedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1PropReactions"""

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


class WebhookIssueCommentEditedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssueCommentEditedPropIssueAllof1PropUser"""

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


model_rebuild(WebhookIssueCommentEditedPropIssueAllof1)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssueCommentEditedPropIssueAllof1",
    "WebhookIssueCommentEditedPropIssueAllof1PropAssignee",
    "WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems",
    "WebhookIssueCommentEditedPropIssueAllof1PropLabelsItems",
    "WebhookIssueCommentEditedPropIssueAllof1PropMilestone",
    "WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssueCommentEditedPropIssueAllof1PropReactions",
    "WebhookIssueCommentEditedPropIssueAllof1PropUser",
)
