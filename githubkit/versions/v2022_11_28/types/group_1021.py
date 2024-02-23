"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoGitTreesPostBodyType(TypedDict):
    """ReposOwnerRepoGitTreesPostBody"""

    tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType]
    base_tree: NotRequired[str]


class ReposOwnerRepoGitTreesPostBodyPropTreeItemsType(TypedDict):
    """ReposOwnerRepoGitTreesPostBodyPropTreeItems"""

    path: NotRequired[str]
    mode: NotRequired[Literal["100644", "100755", "040000", "160000", "120000"]]
    type: NotRequired[Literal["blob", "tree", "commit"]]
    sha: NotRequired[Union[str, None]]
    content: NotRequired[str]


__all__ = (
    "ReposOwnerRepoGitTreesPostBodyType",
    "ReposOwnerRepoGitTreesPostBodyPropTreeItemsType",
)
