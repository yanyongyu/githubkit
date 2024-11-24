"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser


class GistHistory(GitHubModel):
    """Gist History

    Gist History
    """

    user: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    version: Missing[str] = Field(default=UNSET)
    committed_at: Missing[datetime] = Field(default=UNSET)
    change_status: Missing[GistHistoryPropChangeStatus] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class GistHistoryPropChangeStatus(GitHubModel):
    """GistHistoryPropChangeStatus"""

    total: Missing[int] = Field(default=UNSET)
    additions: Missing[int] = Field(default=UNSET)
    deletions: Missing[int] = Field(default=UNSET)


class GistSimplePropForkOf(GitHubModel):
    """Gist

    Gist
    """

    url: str = Field()
    forks_url: str = Field()
    commits_url: str = Field()
    id: str = Field()
    node_id: str = Field()
    git_pull_url: str = Field()
    git_push_url: str = Field()
    html_url: str = Field()
    files: GistSimplePropForkOfPropFiles = Field()
    public: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    description: Union[str, None] = Field()
    comments: int = Field()
    user: Union[None, SimpleUser] = Field()
    comments_url: str = Field()
    owner: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    truncated: Missing[bool] = Field(default=UNSET)
    forks: Missing[list[Any]] = Field(default=UNSET)
    history: Missing[list[Any]] = Field(default=UNSET)


class GistSimplePropForkOfPropFiles(ExtraGitHubModel):
    """GistSimplePropForkOfPropFiles"""


model_rebuild(GistHistory)
model_rebuild(GistHistoryPropChangeStatus)
model_rebuild(GistSimplePropForkOf)
model_rebuild(GistSimplePropForkOfPropFiles)

__all__ = (
    "GistHistory",
    "GistHistoryPropChangeStatus",
    "GistSimplePropForkOf",
    "GistSimplePropForkOfPropFiles",
)
