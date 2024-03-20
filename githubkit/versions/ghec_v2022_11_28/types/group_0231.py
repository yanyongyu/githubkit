"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

from .group_0001 import SimpleUserType
from .group_0017 import RepositoryType


class PullRequestSimplePropHeadType(TypedDict):
    """PullRequestSimplePropHead"""

    label: Union[str, None]
    ref: str
    repo: Union[None, RepositoryType]
    sha: str
    user: Union[None, SimpleUserType]


class PullRequestSimplePropBaseType(TypedDict):
    """PullRequestSimplePropBase"""

    label: str
    ref: str
    repo: RepositoryType
    sha: str
    user: Union[None, SimpleUserType]


__all__ = (
    "PullRequestSimplePropHeadType",
    "PullRequestSimplePropBaseType",
)
