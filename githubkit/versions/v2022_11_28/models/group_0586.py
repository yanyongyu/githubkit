"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0040 import IssueType
from .group_0592 import (
    WebhookIssuesClosedPropIssueAllof0PropPullRequest,
    WebhookIssuesClosedPropIssueAllof0PropSubIssuesSummary,
)
from .group_0594 import WebhookIssuesClosedPropIssueMergedMilestone
from .group_0595 import WebhookIssuesClosedPropIssueMergedPerformedViaGithubApp


class WebhookIssuesClosedPropIssue(GitHubModel):
    """WebhookIssuesClosedPropIssue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ] = Field()
    assignee: Missing[Union[WebhookIssuesClosedPropIssueMergedAssignee, None]] = Field(
        default=UNSET
    )
    assignees: list[WebhookIssuesClosedPropIssueMergedAssignees] = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[Union[str, None], None] = Field(description="Contents of the issue")
    closed_at: Union[datetime, None] = Field()
    comments: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    draft: Missing[bool] = Field(default=UNSET)
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: Missing[list[WebhookIssuesClosedPropIssueMergedLabels]] = Field(
        default=UNSET
    )
    labels_url: str = Field()
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Union[WebhookIssuesClosedPropIssueMergedMilestone, None] = Field()
    node_id: str = Field()
    number: int = Field()
    performed_via_github_app: Missing[
        Union[WebhookIssuesClosedPropIssueMergedPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    pull_request: Missing[WebhookIssuesClosedPropIssueAllof0PropPullRequest] = Field(
        default=UNSET
    )
    reactions: WebhookIssuesClosedPropIssueMergedReactions = Field()
    repository_url: str = Field()
    sub_issues_summary: Missing[
        WebhookIssuesClosedPropIssueAllof0PropSubIssuesSummary
    ] = Field(default=UNSET, title="Sub-issues Summary")
    state: Literal["open", "closed"] = Field(
        description="State of the issue; either 'open' or 'closed'"
    )
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field(description="Title of the issue")
    type: Missing[Union[IssueType, None]] = Field(
        default=UNSET, title="Issue Type", description="The type of issue."
    )
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue")
    user: WebhookIssuesClosedPropIssueMergedUser = Field()


class WebhookIssuesClosedPropIssueMergedAssignee(GitHubModel):
    """WebhookIssuesClosedPropIssueMergedAssignee"""

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


class WebhookIssuesClosedPropIssueMergedAssignees(GitHubModel):
    """WebhookIssuesClosedPropIssueMergedAssignees"""

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


class WebhookIssuesClosedPropIssueMergedLabels(GitHubModel):
    """WebhookIssuesClosedPropIssueMergedLabels"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssuesClosedPropIssueMergedReactions(GitHubModel):
    """WebhookIssuesClosedPropIssueMergedReactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookIssuesClosedPropIssueMergedUser(GitHubModel):
    """WebhookIssuesClosedPropIssueMergedUser"""

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


model_rebuild(WebhookIssuesClosedPropIssue)
model_rebuild(WebhookIssuesClosedPropIssueMergedAssignee)
model_rebuild(WebhookIssuesClosedPropIssueMergedAssignees)
model_rebuild(WebhookIssuesClosedPropIssueMergedLabels)
model_rebuild(WebhookIssuesClosedPropIssueMergedReactions)
model_rebuild(WebhookIssuesClosedPropIssueMergedUser)

__all__ = (
    "WebhookIssuesClosedPropIssue",
    "WebhookIssuesClosedPropIssueMergedAssignee",
    "WebhookIssuesClosedPropIssueMergedAssignees",
    "WebhookIssuesClosedPropIssueMergedLabels",
    "WebhookIssuesClosedPropIssueMergedReactions",
    "WebhookIssuesClosedPropIssueMergedUser",
)
