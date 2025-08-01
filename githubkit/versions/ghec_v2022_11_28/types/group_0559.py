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
from .group_0487 import EnterpriseWebhooksType
from .group_0488 import SimpleInstallationType
from .group_0489 import OrganizationSimpleWebhooksType
from .group_0490 import RepositoryWebhooksType


class WebhookCheckSuiteRequestedType(TypedDict):
    """check_suite requested event"""

    action: Literal["requested"]
    check_suite: WebhookCheckSuiteRequestedPropCheckSuiteType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookCheckSuiteRequestedPropCheckSuiteType(TypedDict):
    """WebhookCheckSuiteRequestedPropCheckSuite

    The [check_suite](https://docs.github.com/enterprise-
    cloud@latest//rest/checks/suites#get-a-check-suite).
    """

    after: Union[str, None]
    app: WebhookCheckSuiteRequestedPropCheckSuitePropAppType
    before: Union[str, None]
    check_runs_url: str
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
        ],
    ]
    created_at: datetime
    head_branch: Union[str, None]
    head_commit: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitType
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: list[
        WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsType
    ]
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]
    status: Union[None, Literal["requested", "in_progress", "completed", "queued"]]
    updated_at: datetime
    url: str


class WebhookCheckSuiteRequestedPropCheckSuitePropAppType(TypedDict):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    client_id: NotRequired[Union[str, None]]
    name: str
    node_id: str
    owner: Union[WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwnerType, None]
    permissions: NotRequired[
        WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwnerType(TypedDict):
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
    user_view_type: NotRequired[str]


class WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissionsType(TypedDict):
    """WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitType(TypedDict):
    """SimpleCommit"""

    author: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthorType
    committer: WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitterType
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitterType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsType(TypedDict):
    """Check Run Pull Request"""

    base: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBaseType
    head: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadType
    id: int
    number: int
    url: str


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookCheckSuiteRequestedPropCheckSuitePropAppPropOwnerType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropAppPropPermissionsType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropAppType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropAuthorType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitPropCommitterType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropHeadCommitType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropBaseType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsPropHeadType",
    "WebhookCheckSuiteRequestedPropCheckSuitePropPullRequestsItemsType",
    "WebhookCheckSuiteRequestedPropCheckSuiteType",
    "WebhookCheckSuiteRequestedType",
)
