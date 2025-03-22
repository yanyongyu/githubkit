"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0003 import SimpleUser
from .group_0020 import Repository


class PullRequestPropHead(GitHubModel):
    """PullRequestPropHead"""

    label: Union[str, None] = Field()
    ref: str = Field()
    repo: Repository = Field(title="Repository", description="A repository on GitHub.")
    sha: str = Field()
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class PullRequestPropBase(GitHubModel):
    """PullRequestPropBase"""

    label: str = Field()
    ref: str = Field()
    repo: Repository = Field(title="Repository", description="A repository on GitHub.")
    sha: str = Field()
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(PullRequestPropHead)
model_rebuild(PullRequestPropBase)

__all__ = (
    "PullRequestPropBase",
    "PullRequestPropHead",
)
