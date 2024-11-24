"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class Root(GitHubModel):
    """Root"""

    current_user_url: str = Field()
    current_user_authorizations_html_url: str = Field()
    authorizations_url: str = Field()
    code_search_url: str = Field()
    commit_search_url: str = Field()
    emails_url: str = Field()
    emojis_url: str = Field()
    events_url: str = Field()
    feeds_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    hub_url: Missing[str] = Field(default=UNSET)
    issue_search_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    label_search_url: str = Field()
    notifications_url: str = Field()
    organization_url: str = Field()
    organization_repositories_url: str = Field()
    organization_teams_url: str = Field()
    public_gists_url: str = Field()
    rate_limit_url: str = Field()
    repository_url: str = Field()
    repository_search_url: str = Field()
    current_user_repositories_url: str = Field()
    starred_url: str = Field()
    starred_gists_url: str = Field()
    topic_search_url: Missing[str] = Field(default=UNSET)
    user_url: str = Field()
    user_organizations_url: str = Field()
    user_repositories_url: str = Field()
    user_search_url: str = Field()


model_rebuild(Root)

__all__ = ("Root",)
