"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0017 import Repository


class PullRequestSimplePropHead(GitHubModel):
    """PullRequestSimplePropHead"""

    label: Union[str, None] = Field()
    ref: str = Field()
    repo: Union[None, Repository] = Field()
    sha: str = Field()
    user: Union[None, SimpleUser] = Field()


class PullRequestSimplePropBase(GitHubModel):
    """PullRequestSimplePropBase"""

    label: str = Field()
    ref: str = Field()
    repo: Repository = Field(title="Repository", description="A repository on GitHub.")
    sha: str = Field()
    user: Union[None, SimpleUser] = Field()


model_rebuild(PullRequestSimplePropHead)
model_rebuild(PullRequestSimplePropBase)

__all__ = (
    "PullRequestSimplePropHead",
    "PullRequestSimplePropBase",
)