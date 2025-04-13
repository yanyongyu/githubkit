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

from .group_0003 import SimpleUser
from .group_0472 import EnterpriseWebhooks
from .group_0473 import SimpleInstallation
from .group_0474 import OrganizationSimpleWebhooks
from .group_0475 import RepositoryWebhooks


class WebhookStatus(GitHubModel):
    """status event"""

    avatar_url: Missing[Union[str, None]] = Field(default=UNSET)
    branches: list[WebhookStatusPropBranchesItems] = Field(
        description="An array of branch objects containing the status' SHA. Each branch contains the given SHA, but the SHA may or may not be the head of the branch. The array includes a maximum of 10 branches."
    )
    commit: WebhookStatusPropCommit = Field()
    context: str = Field()
    created_at: str = Field()
    description: Union[str, None] = Field(
        description="The optional human-readable description added to the status."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    id: int = Field(description="The unique identifier of the status.")
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    name: str = Field()
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
    sha: str = Field(description="The Commit SHA.")
    state: Literal["pending", "success", "failure", "error"] = Field(
        description="The new state. Can be `pending`, `success`, `failure`, or `error`."
    )
    target_url: Union[str, None] = Field(
        description="The optional link added to the status."
    )
    updated_at: str = Field()


class WebhookStatusPropBranchesItems(GitHubModel):
    """WebhookStatusPropBranchesItems"""

    commit: WebhookStatusPropBranchesItemsPropCommit = Field()
    name: str = Field()
    protected: bool = Field()


class WebhookStatusPropBranchesItemsPropCommit(GitHubModel):
    """WebhookStatusPropBranchesItemsPropCommit"""

    sha: Union[str, None] = Field()
    url: Union[str, None] = Field()


class WebhookStatusPropCommit(GitHubModel):
    """WebhookStatusPropCommit"""

    author: Union[WebhookStatusPropCommitPropAuthor, None] = Field(title="User")
    comments_url: str = Field()
    commit: WebhookStatusPropCommitPropCommit = Field()
    committer: Union[WebhookStatusPropCommitPropCommitter, None] = Field(title="User")
    html_url: str = Field()
    node_id: str = Field()
    parents: list[WebhookStatusPropCommitPropParentsItems] = Field()
    sha: str = Field()
    url: str = Field()


class WebhookStatusPropCommitPropAuthor(GitHubModel):
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
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
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


class WebhookStatusPropCommitPropCommitter(GitHubModel):
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
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
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


class WebhookStatusPropCommitPropParentsItems(GitHubModel):
    """WebhookStatusPropCommitPropParentsItems"""

    html_url: str = Field()
    sha: str = Field()
    url: str = Field()


class WebhookStatusPropCommitPropCommit(GitHubModel):
    """WebhookStatusPropCommitPropCommit"""

    author: WebhookStatusPropCommitPropCommitPropAuthor = Field()
    comment_count: int = Field()
    committer: WebhookStatusPropCommitPropCommitPropCommitter = Field()
    message: str = Field()
    tree: WebhookStatusPropCommitPropCommitPropTree = Field()
    url: str = Field()
    verification: WebhookStatusPropCommitPropCommitPropVerification = Field()


class WebhookStatusPropCommitPropCommitPropAuthor(GitHubModel):
    """WebhookStatusPropCommitPropCommitPropAuthor"""

    date: datetime = Field()
    email: str = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookStatusPropCommitPropCommitPropCommitter(GitHubModel):
    """WebhookStatusPropCommitPropCommitPropCommitter"""

    date: datetime = Field()
    email: str = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookStatusPropCommitPropCommitPropTree(GitHubModel):
    """WebhookStatusPropCommitPropCommitPropTree"""

    sha: str = Field()
    url: str = Field()


class WebhookStatusPropCommitPropCommitPropVerification(GitHubModel):
    """WebhookStatusPropCommitPropCommitPropVerification"""

    payload: Union[str, None] = Field()
    reason: Literal[
        "expired_key",
        "not_signing_key",
        "gpgverify_error",
        "gpgverify_unavailable",
        "unsigned",
        "unknown_signature_type",
        "no_user",
        "unverified_email",
        "bad_email",
        "unknown_key",
        "malformed_signature",
        "invalid",
        "valid",
        "bad_cert",
        "ocsp_pending",
    ] = Field()
    signature: Union[str, None] = Field()
    verified: bool = Field()
    verified_at: Union[str, None] = Field()


model_rebuild(WebhookStatus)
model_rebuild(WebhookStatusPropBranchesItems)
model_rebuild(WebhookStatusPropBranchesItemsPropCommit)
model_rebuild(WebhookStatusPropCommit)
model_rebuild(WebhookStatusPropCommitPropAuthor)
model_rebuild(WebhookStatusPropCommitPropCommitter)
model_rebuild(WebhookStatusPropCommitPropParentsItems)
model_rebuild(WebhookStatusPropCommitPropCommit)
model_rebuild(WebhookStatusPropCommitPropCommitPropAuthor)
model_rebuild(WebhookStatusPropCommitPropCommitPropCommitter)
model_rebuild(WebhookStatusPropCommitPropCommitPropTree)
model_rebuild(WebhookStatusPropCommitPropCommitPropVerification)

__all__ = (
    "WebhookStatus",
    "WebhookStatusPropBranchesItems",
    "WebhookStatusPropBranchesItemsPropCommit",
    "WebhookStatusPropCommit",
    "WebhookStatusPropCommitPropAuthor",
    "WebhookStatusPropCommitPropCommit",
    "WebhookStatusPropCommitPropCommitPropAuthor",
    "WebhookStatusPropCommitPropCommitPropCommitter",
    "WebhookStatusPropCommitPropCommitPropTree",
    "WebhookStatusPropCommitPropCommitPropVerification",
    "WebhookStatusPropCommitPropCommitter",
    "WebhookStatusPropCommitPropParentsItems",
)
