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


class WebhookIssuesClosedPropIssueAllof1(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1"""

    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Missing[Union[WebhookIssuesClosedPropIssueAllof1PropAssignee, None]] = (
        Field(default=UNSET)
    )
    assignees: Missing[
        list[Union[WebhookIssuesClosedPropIssueAllof1PropAssigneesItems, None]]
    ] = Field(default=UNSET)
    author_association: Missing[str] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(default=UNSET)
    closed_at: Union[str, None] = Field()
    comments: Missing[int] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: Missing[
        list[Union[WebhookIssuesClosedPropIssueAllof1PropLabelsItems, None]]
    ] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Missing[Union[WebhookIssuesClosedPropIssueAllof1PropMilestone, None]] = (
        Field(default=UNSET)
    )
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssuesClosedPropIssueAllof1PropReactions] = Field(
        default=UNSET
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Literal["closed", "open"] = Field()
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookIssuesClosedPropIssueAllof1PropUser] = Field(default=UNSET)


class WebhookIssuesClosedPropIssueAllof1PropAssignee(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropAssignee"""


class WebhookIssuesClosedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesClosedPropIssueAllof1PropLabelsItems(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesClosedPropIssueAllof1PropMilestone(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropMilestone"""


class WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesClosedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropReactions"""

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


class WebhookIssuesClosedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssuesClosedPropIssueAllof1PropUser"""

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
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesClosedPropIssueAllof1)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssuesClosedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssuesClosedPropIssueAllof1",
    "WebhookIssuesClosedPropIssueAllof1PropAssignee",
    "WebhookIssuesClosedPropIssueAllof1PropAssigneesItems",
    "WebhookIssuesClosedPropIssueAllof1PropLabelsItems",
    "WebhookIssuesClosedPropIssueAllof1PropMilestone",
    "WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssuesClosedPropIssueAllof1PropReactions",
    "WebhookIssuesClosedPropIssueAllof1PropUser",
)
