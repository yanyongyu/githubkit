"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0487 import EnterpriseWebhooks
from .group_0488 import SimpleInstallation
from .group_0489 import OrganizationSimpleWebhooks
from .group_0490 import RepositoryWebhooks


class WebhookCommitCommentCreated(GitHubModel):
    """commit_comment created event"""

    action: Literal["created"] = Field(
        description="The action performed. Can be `created`."
    )
    comment: WebhookCommitCommentCreatedPropComment = Field(
        description="The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookCommitCommentCreatedPropComment(GitHubModel):
    """WebhookCommitCommentCreatedPropComment

    The [commit
    comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-
    comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource.
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
    body: str = Field(description="The text of the comment.")
    commit_id: str = Field(
        description="The SHA of the commit to which the comment applies."
    )
    created_at: str = Field()
    html_url: str = Field()
    id: int = Field(description="The ID of the commit comment.")
    line: Union[int, None] = Field(
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment"
    )
    node_id: str = Field(description="The node ID of the commit comment.")
    path: Union[str, None] = Field(
        description="The relative path of the file to which the comment applies."
    )
    position: Union[int, None] = Field(
        description="The line index in the diff to which the comment applies."
    )
    reactions: Missing[WebhookCommitCommentCreatedPropCommentPropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    updated_at: str = Field()
    url: str = Field()
    user: Union[WebhookCommitCommentCreatedPropCommentPropUser, None] = Field(
        title="User"
    )


class WebhookCommitCommentCreatedPropCommentPropReactions(GitHubModel):
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


class WebhookCommitCommentCreatedPropCommentPropUser(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookCommitCommentCreated)
model_rebuild(WebhookCommitCommentCreatedPropComment)
model_rebuild(WebhookCommitCommentCreatedPropCommentPropReactions)
model_rebuild(WebhookCommitCommentCreatedPropCommentPropUser)

__all__ = (
    "WebhookCommitCommentCreated",
    "WebhookCommitCommentCreatedPropComment",
    "WebhookCommitCommentCreatedPropCommentPropReactions",
    "WebhookCommitCommentCreatedPropCommentPropUser",
)
