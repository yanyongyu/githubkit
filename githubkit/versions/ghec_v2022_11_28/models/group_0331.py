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


class GitTree(GitHubModel):
    """Git Tree

    The hierarchy between files in a Git repository.
    """

    sha: str = Field()
    url: str = Field()
    truncated: bool = Field()
    tree: list[GitTreePropTreeItems] = Field(
        description="Objects specifying a tree structure"
    )


class GitTreePropTreeItems(GitHubModel):
    """GitTreePropTreeItems"""

    path: Missing[str] = Field(default=UNSET)
    mode: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)
    size: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(GitTree)
model_rebuild(GitTreePropTreeItems)

__all__ = (
    "GitTree",
    "GitTreePropTreeItems",
)
