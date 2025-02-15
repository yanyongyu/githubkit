"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0404 import EnterpriseWebhooksType
from .group_0405 import SimpleInstallationType
from .group_0406 import OrganizationSimpleWebhooksType
from .group_0407 import RepositoryWebhooksType


class WebhookStatusType(TypedDict):
    """status event"""

    avatar_url: NotRequired[Union[str, None]]
    branches: list[WebhookStatusPropBranchesItemsType]
    commit: WebhookStatusPropCommitType
    context: str
    created_at: str
    description: Union[str, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    id: int
    installation: NotRequired[SimpleInstallationType]
    name: str
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    sha: str
    state: Literal["pending", "success", "failure", "error"]
    target_url: Union[str, None]
    updated_at: str


class WebhookStatusPropBranchesItemsType(TypedDict):
    """WebhookStatusPropBranchesItems"""

    commit: WebhookStatusPropBranchesItemsPropCommitType
    name: str
    protected: bool


class WebhookStatusPropBranchesItemsPropCommitType(TypedDict):
    """WebhookStatusPropBranchesItemsPropCommit"""

    sha: Union[str, None]
    url: Union[str, None]


class WebhookStatusPropCommitType(TypedDict):
    """WebhookStatusPropCommit"""

    author: Union[WebhookStatusPropCommitPropAuthorType, None]
    comments_url: str
    commit: WebhookStatusPropCommitPropCommitType
    committer: Union[WebhookStatusPropCommitPropCommitterType, None]
    html_url: str
    node_id: str
    parents: list[WebhookStatusPropCommitPropParentsItemsType]
    sha: str
    url: str


class WebhookStatusPropCommitPropAuthorType(TypedDict):
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
    id: NotRequired[int]
    login: NotRequired[str]
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


class WebhookStatusPropCommitPropCommitterType(TypedDict):
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
    id: NotRequired[int]
    login: NotRequired[str]
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


class WebhookStatusPropCommitPropParentsItemsType(TypedDict):
    """WebhookStatusPropCommitPropParentsItems"""

    html_url: str
    sha: str
    url: str


class WebhookStatusPropCommitPropCommitType(TypedDict):
    """WebhookStatusPropCommitPropCommit"""

    author: WebhookStatusPropCommitPropCommitPropAuthorType
    comment_count: int
    committer: WebhookStatusPropCommitPropCommitPropCommitterType
    message: str
    tree: WebhookStatusPropCommitPropCommitPropTreeType
    url: str
    verification: WebhookStatusPropCommitPropCommitPropVerificationType


class WebhookStatusPropCommitPropCommitPropAuthorType(TypedDict):
    """WebhookStatusPropCommitPropCommitPropAuthor"""

    date: datetime
    email: str
    name: str
    username: NotRequired[str]


class WebhookStatusPropCommitPropCommitPropCommitterType(TypedDict):
    """WebhookStatusPropCommitPropCommitPropCommitter"""

    date: datetime
    email: str
    name: str
    username: NotRequired[str]


class WebhookStatusPropCommitPropCommitPropTreeType(TypedDict):
    """WebhookStatusPropCommitPropCommitPropTree"""

    sha: str
    url: str


class WebhookStatusPropCommitPropCommitPropVerificationType(TypedDict):
    """WebhookStatusPropCommitPropCommitPropVerification"""

    payload: Union[str, None]
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
    ]
    signature: Union[str, None]
    verified: bool
    verified_at: Union[str, None]


__all__ = (
    "WebhookStatusPropBranchesItemsPropCommitType",
    "WebhookStatusPropBranchesItemsType",
    "WebhookStatusPropCommitPropAuthorType",
    "WebhookStatusPropCommitPropCommitPropAuthorType",
    "WebhookStatusPropCommitPropCommitPropCommitterType",
    "WebhookStatusPropCommitPropCommitPropTreeType",
    "WebhookStatusPropCommitPropCommitPropVerificationType",
    "WebhookStatusPropCommitPropCommitType",
    "WebhookStatusPropCommitPropCommitterType",
    "WebhookStatusPropCommitPropParentsItemsType",
    "WebhookStatusPropCommitType",
    "WebhookStatusType",
)
