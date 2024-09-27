"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0419 import SimpleUserWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType


class WebhookPullRequestAutoMergeDisabledType(TypedDict):
    """pull_request auto_merge_disabled event"""

    action: Literal["auto_merge_disabled"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestAutoMergeDisabledPropPullRequestType
    reason: str
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookPullRequestAutoMergeDisabledPropPullRequestType(TypedDict):
    """Pull Request"""

    links: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    additions: NotRequired[int]
    assignee: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneeType, None
    ]
    assignees: List[
        Union[
            WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneesItemsType,
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
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergeType, None
    ]
    base: WebhookPullRequestAutoMergeDisabledPropPullRequestPropBaseType
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
    head: WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[WebhookPullRequestAutoMergeDisabledPropPullRequestPropLabelsItemsType]
    locked: bool
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Union[str, None]
    mergeable: NotRequired[Union[bool, None]]
    mergeable_state: NotRequired[str]
    merged: NotRequired[Union[bool, None]]
    merged_at: Union[datetime, None]
    merged_by: NotRequired[
        Union[WebhookPullRequestAutoMergeDisabledPropPullRequestPropMergedByType, None]
    ]
    milestone: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    rebaseable: NotRequired[Union[bool, None]]
    requested_reviewers: List[
        Union[
            WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments: NotRequired[int]
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookPullRequestAutoMergeDisabledPropPullRequestPropUserType, None]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneeType(TypedDict):
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneesItemsType(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergeType(TypedDict):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergePropEnabledByType(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropMergedByType(TypedDict):
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestonePropCreatorType,
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestonePropCreatorType(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof0Type(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropUserType(TypedDict):
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinks"""

    comments: (
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommentsType
    )
    commits: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommitsType
    html: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropIssueType
    review_comment: (
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentType
    )
    review_comments: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentsType
    self_: WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropSelfType
    statuses: (
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropStatusesType
    )


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropUserType, None
    ]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropUserType(TypedDict):
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoType(TypedDict):
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
    has_discussions: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
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
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropLicenseType,
        None,
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
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropPermissionsType
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropOwnerType(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropPermission
    s
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropHead"""

    label: str
    ref: str
    repo: WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoType
    sha: str
    user: Union[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropUserType, None
    ]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropUserType(TypedDict):
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoType(TypedDict):
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
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropLicenseType,
        None,
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
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropPermissionsType
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropOwnerType(
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropPermission
    s
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1Type(
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
            WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOne
    of1PropParent
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


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsType(
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
            WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsPropPar
    ent
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


__all__ = (
    "WebhookPullRequestAutoMergeDisabledType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneeType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergeType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropMergedByType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestoneType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropUserType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBaseType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropUserType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestAutoMergeDisabledPropPullRequestPropRequestedTeamsItemsPropParentType",
)
