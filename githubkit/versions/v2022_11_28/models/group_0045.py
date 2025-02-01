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

from .group_0003 import SimpleUser


class BaseGist(GitHubModel):
    """Base Gist

    Base Gist
    """

    url: str = Field()
    forks_url: str = Field()
    commits_url: str = Field()
    id: str = Field()
    node_id: str = Field()
    git_pull_url: str = Field()
    git_push_url: str = Field()
    html_url: str = Field()
    files: BaseGistPropFiles = Field()
    public: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    description: Union[str, None] = Field()
    comments: int = Field()
    comments_enabled: Missing[bool] = Field(default=UNSET)
    user: Union[None, SimpleUser] = Field()
    comments_url: str = Field()
    owner: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    truncated: Missing[bool] = Field(default=UNSET)
    forks: Missing[list[Any]] = Field(default=UNSET)
    history: Missing[list[Any]] = Field(default=UNSET)


class BaseGistPropFiles(ExtraGitHubModel):
    """BaseGistPropFiles"""


model_rebuild(BaseGist)
model_rebuild(BaseGistPropFiles)

__all__ = (
    "BaseGist",
    "BaseGistPropFiles",
)
