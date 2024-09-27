"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookPullRequestReviewThreadUnresolvedType(TypedDict):
    """pull_request_review_thread unresolved event"""

    action: Literal["unresolved"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewThreadUnresolvedPropPullRequestType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]
    thread: WebhookPullRequestReviewThreadUnresolvedPropThreadType


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestType(TypedDict):
    """Simple Pull Request"""

    links: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneeType, None
    ]
    assignees: List[
        Union[
            WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneesItemsType,
            None,
        ]
    ]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergeType, None
    ]
    base: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBaseType
    body: Union[str, None]
    closed_at: Union[str, None]
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLabelsItemsType
    ]
    locked: bool
    merge_commit_sha: Union[str, None]
    merged_at: Union[str, None]
    milestone: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: List[
        Union[
            WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropUserType, None
    ]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneeType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneesItemsType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergeType(
    TypedDict
):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: str
    enabled_by: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergePropEnabledByType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLabelsItemsType(
    TypedDict
):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestoneType(
    TypedDict
):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestonePropCreatorType,
        None,
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestonePropCreatorType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof0Type(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropUserType(TypedDict):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinks"""

    comments: (
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommentsType
    )
    commits: (
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommitsType
    )
    html: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentsType
    self_: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropSelfType
    statuses: (
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropStatusesType
    )


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropUserType,
        None,
    ]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropPermi
    ssions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHead"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropUserType,
        None,
    ]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropPermi
    ssions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersIte
    msOneof1PropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsPr
    opParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewThreadUnresolvedPropThreadType(TypedDict):
    """WebhookPullRequestReviewThreadUnresolvedPropThread"""

    comments: List[
        WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsType
    ]
    node_id: str


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsType(
    TypedDict
):
    """Pull Request Review Comment

    The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-
    for-a-pull-request) itself.
    """

    links: (
        WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksType
    )
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: str
    commit_id: str
    created_at: datetime
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: NotRequired[int]
    line: Union[int, None]
    node_id: str
    original_commit_id: str
    original_line: int
    original_position: int
    original_start_line: Union[int, None]
    path: str
    position: Union[int, None]
    pull_request_review_id: Union[int, None]
    pull_request_url: str
    reactions: WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropReactionsType
    side: Literal["LEFT", "RIGHT"]
    start_line: Union[int, None]
    start_side: Union[None, Literal["LEFT", "RIGHT"]]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: datetime
    url: str
    user: Union[
        WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropUserType,
        None,
    ]


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropReactionsType(
    TypedDict
):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksType(
    TypedDict
):
    """WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinks"""

    html: WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropHtmlType
    pull_request: WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType
    self_: WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropSelfType


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


__all__ = (
    "WebhookPullRequestReviewThreadUnresolvedType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropUserType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBaseType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewThreadUnresolvedPropPullRequestPropRequestedTeamsItemsPropParentType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropReactionsType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropUserType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropHtmlType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType",
    "WebhookPullRequestReviewThreadUnresolvedPropThreadPropCommentsItemsPropLinksPropSelfType",
)
