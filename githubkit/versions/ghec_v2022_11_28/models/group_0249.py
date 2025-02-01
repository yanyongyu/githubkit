"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0245 import GitUser
from .group_0246 import Verification


class CommitPropCommit(GitHubModel):
    """CommitPropCommit"""

    url: str = Field()
    author: Union[None, GitUser] = Field()
    committer: Union[None, GitUser] = Field()
    message: str = Field()
    comment_count: int = Field()
    tree: CommitPropCommitPropTree = Field()
    verification: Missing[Verification] = Field(default=UNSET, title="Verification")


class CommitPropCommitPropTree(GitHubModel):
    """CommitPropCommitPropTree"""

    sha: str = Field()
    url: str = Field()


model_rebuild(CommitPropCommit)
model_rebuild(CommitPropCommitPropTree)

__all__ = (
    "CommitPropCommit",
    "CommitPropCommitPropTree",
)
