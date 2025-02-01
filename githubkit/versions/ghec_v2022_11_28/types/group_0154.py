"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0153 import SecurityAndAnalysisType


class MinimalRepositoryType(TypedDict):
    """Minimal Repository

    Minimal Repository
    """

    id: int
    node_id: str
    name: str
    full_name: str
    owner: SimpleUserType
    private: bool
    html_url: str
    description: Union[str, None]
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: NotRequired[str]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: NotRequired[str]
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: NotRequired[str]
    mirror_url: NotRequired[Union[str, None]]
    hooks_url: str
    svn_url: NotRequired[str]
    homepage: NotRequired[Union[str, None]]
    language: NotRequired[Union[str, None]]
    forks_count: NotRequired[int]
    stargazers_count: NotRequired[int]
    watchers_count: NotRequired[int]
    size: NotRequired[int]
    default_branch: NotRequired[str]
    open_issues_count: NotRequired[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    has_pages: NotRequired[bool]
    has_downloads: NotRequired[bool]
    has_discussions: NotRequired[bool]
    archived: NotRequired[bool]
    disabled: NotRequired[bool]
    visibility: NotRequired[str]
    pushed_at: NotRequired[Union[datetime, None]]
    created_at: NotRequired[Union[datetime, None]]
    updated_at: NotRequired[Union[datetime, None]]
    permissions: NotRequired[MinimalRepositoryPropPermissionsType]
    role_name: NotRequired[str]
    temp_clone_token: NotRequired[Union[str, None]]
    delete_branch_on_merge: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    code_of_conduct: NotRequired[CodeOfConductType]
    license_: NotRequired[Union[MinimalRepositoryPropLicenseType, None]]
    forks: NotRequired[int]
    open_issues: NotRequired[int]
    watchers: NotRequired[int]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    security_and_analysis: NotRequired[Union[SecurityAndAnalysisType, None]]


class CodeOfConductType(TypedDict):
    """Code Of Conduct

    Code Of Conduct
    """

    key: str
    name: str
    url: str
    body: NotRequired[str]
    html_url: Union[str, None]


class MinimalRepositoryPropPermissionsType(TypedDict):
    """MinimalRepositoryPropPermissions"""

    admin: NotRequired[bool]
    maintain: NotRequired[bool]
    push: NotRequired[bool]
    triage: NotRequired[bool]
    pull: NotRequired[bool]


class MinimalRepositoryPropLicenseType(TypedDict):
    """MinimalRepositoryPropLicense"""

    key: NotRequired[str]
    name: NotRequired[str]
    spdx_id: NotRequired[str]
    url: NotRequired[str]
    node_id: NotRequired[str]


__all__ = (
    "CodeOfConductType",
    "MinimalRepositoryPropLicenseType",
    "MinimalRepositoryPropPermissionsType",
    "MinimalRepositoryType",
)
