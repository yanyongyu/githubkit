"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0005 import Integration


class WebhookIssueCommentCreatedPropComment(GitHubModel):
    """issue comment

    The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment)
    itself.
    """

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
    body: str = Field(description="Contents of the issue comment")
    created_at: datetime = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the issue comment")
    issue_url: str = Field()
    node_id: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    reactions: WebhookIssueCommentCreatedPropCommentPropReactions = Field(
        title="Reactions"
    )
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue comment")
    user: Union[WebhookIssueCommentCreatedPropCommentPropUser, None] = Field(
        title="User"
    )


class WebhookIssueCommentCreatedPropCommentPropReactions(GitHubModel):
    """Reactions"""

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


class WebhookIssueCommentCreatedPropCommentPropUser(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssueCommentCreatedPropComment)
model_rebuild(WebhookIssueCommentCreatedPropCommentPropReactions)
model_rebuild(WebhookIssueCommentCreatedPropCommentPropUser)

__all__ = (
    "WebhookIssueCommentCreatedPropComment",
    "WebhookIssueCommentCreatedPropCommentPropReactions",
    "WebhookIssueCommentCreatedPropCommentPropUser",
)
