"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0416 import WebhooksUserType
from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookPullRequestAssignedType(TypedDict):
    """pull_request assigned event"""

    action: Literal["assigned"]
    assignee: Union[WebhooksUserType, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestAssignedPropPullRequestType
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookPullRequestAssignedPropPullRequestType(TypedDict):
    """Pull Request"""

    links: WebhookPullRequestAssignedPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    additions: NotRequired[int]
    assignee: Union[WebhookPullRequestAssignedPropPullRequestPropAssigneeType, None]
    assignees: List[
        Union[WebhookPullRequestAssignedPropPullRequestPropAssigneesItemsType, None]
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
    auto_merge: Union[WebhookPullRequestAssignedPropPullRequestPropAutoMergeType, None]
    base: WebhookPullRequestAssignedPropPullRequestPropBaseType
    body: Union[str, None]
    changed_files: NotRequired[int]
    closed_at: Union[datetime, None]
    comments: NotRequired[int]
    comments_url: str
    commits: NotRequired[int]
    commits_url: str
    created_at: datetime
    deletions: NotRequired[int]
    diff_url: str
    draft: bool
    head: WebhookPullRequestAssignedPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[WebhookPullRequestAssignedPropPullRequestPropLabelsItemsType]
    locked: bool
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Union[str, None]
    mergeable: NotRequired[Union[bool, None]]
    mergeable_state: NotRequired[str]
    merged: NotRequired[Union[bool, None]]
    merged_at: Union[datetime, None]
    merged_by: NotRequired[
        Union[WebhookPullRequestAssignedPropPullRequestPropMergedByType, None]
    ]
    milestone: Union[WebhookPullRequestAssignedPropPullRequestPropMilestoneType, None]
    node_id: str
    number: int
    patch_url: str
    rebaseable: NotRequired[Union[bool, None]]
    requested_reviewers: List[
        Union[
            WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments: NotRequired[int]
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookPullRequestAssignedPropPullRequestPropUserType, None]


class WebhookPullRequestAssignedPropPullRequestPropAssigneeType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropAssigneesItemsType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropAutoMergeType(TypedDict):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestAssignedPropPullRequestPropAutoMergePropEnabledByType, None
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestAssignedPropPullRequestPropAutoMergePropEnabledByType(
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


class WebhookPullRequestAssignedPropPullRequestPropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestAssignedPropPullRequestPropMergedByType(TypedDict):
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


class WebhookPullRequestAssignedPropPullRequestPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestAssignedPropPullRequestPropMilestonePropCreatorType, None
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


class WebhookPullRequestAssignedPropPullRequestPropMilestonePropCreatorType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof0Type(
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropUserType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestAssignedPropPullRequestPropLinks"""

    comments: WebhookPullRequestAssignedPropPullRequestPropLinksPropCommentsType
    commits: WebhookPullRequestAssignedPropPullRequestPropLinksPropCommitsType
    html: WebhookPullRequestAssignedPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestAssignedPropPullRequestPropLinksPropIssueType
    review_comment: (
        WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentType
    )
    review_comments: (
        WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentsType
    )
    self_: WebhookPullRequestAssignedPropPullRequestPropLinksPropSelfType
    statuses: WebhookPullRequestAssignedPropPullRequestPropLinksPropStatusesType


class WebhookPullRequestAssignedPropPullRequestPropLinksPropCommentsType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropCommitsType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropHtmlType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropIssueType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropSelfType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropLinksPropStatusesType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestAssignedPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestAssignedPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestAssignedPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[WebhookPullRequestAssignedPropPullRequestPropBasePropUserType, None]


class WebhookPullRequestAssignedPropPullRequestPropBasePropUserType(TypedDict):
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


class WebhookPullRequestAssignedPropPullRequestPropBasePropRepoType(TypedDict):
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
        WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropLicenseType, None
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
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
        WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
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
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropOwnerType(TypedDict):
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


class WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestAssignedPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestAssignedPropPullRequestPropHead"""

    label: Union[str, None]
    ref: str
    repo: Union[WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoType, None]
    sha: str
    user: Union[WebhookPullRequestAssignedPropPullRequestPropHeadPropUserType, None]


class WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoType(TypedDict):
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
        WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropLicenseType, None
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
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
        WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
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
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropOwnerType(TypedDict):
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


class WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestAssignedPropPullRequestPropHeadPropUserType(TypedDict):
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


class WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1PropPa
    rent
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


class WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsType(TypedDict):
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
            WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsPropParent"""

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


__all__ = (
    "WebhookPullRequestAssignedType",
    "WebhookPullRequestAssignedPropPullRequestType",
    "WebhookPullRequestAssignedPropPullRequestPropAssigneeType",
    "WebhookPullRequestAssignedPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestAssignedPropPullRequestPropAutoMergeType",
    "WebhookPullRequestAssignedPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestAssignedPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestAssignedPropPullRequestPropMergedByType",
    "WebhookPullRequestAssignedPropPullRequestPropMilestoneType",
    "WebhookPullRequestAssignedPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestAssignedPropPullRequestPropUserType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestAssignedPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestAssignedPropPullRequestPropBaseType",
    "WebhookPullRequestAssignedPropPullRequestPropBasePropUserType",
    "WebhookPullRequestAssignedPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestAssignedPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestAssignedPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestAssignedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestAssignedPropPullRequestPropRequestedTeamsItemsPropParentType",
)
