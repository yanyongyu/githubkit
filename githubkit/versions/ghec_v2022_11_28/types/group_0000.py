"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class RootType(TypedDict):
    """Root"""

    current_user_url: str
    current_user_authorizations_html_url: str
    authorizations_url: str
    code_search_url: str
    commit_search_url: str
    emails_url: str
    emojis_url: str
    events_url: str
    feeds_url: str
    followers_url: str
    following_url: str
    gists_url: str
    hub_url: NotRequired[str]
    issue_search_url: str
    issues_url: str
    keys_url: str
    label_search_url: str
    notifications_url: str
    organization_url: str
    organization_repositories_url: str
    organization_teams_url: str
    public_gists_url: str
    rate_limit_url: str
    repository_url: str
    repository_search_url: str
    current_user_repositories_url: str
    starred_url: str
    starred_gists_url: str
    topic_search_url: NotRequired[str]
    user_url: str
    user_organizations_url: str
    user_repositories_url: str
    user_search_url: str


__all__ = ("RootType",)
