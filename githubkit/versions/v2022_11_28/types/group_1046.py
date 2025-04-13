"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoContentsPathDeleteBodyType(TypedDict):
    """ReposOwnerRepoContentsPathDeleteBody"""

    message: str
    sha: str
    branch: NotRequired[str]
    committer: NotRequired[ReposOwnerRepoContentsPathDeleteBodyPropCommitterType]
    author: NotRequired[ReposOwnerRepoContentsPathDeleteBodyPropAuthorType]


class ReposOwnerRepoContentsPathDeleteBodyPropCommitterType(TypedDict):
    """ReposOwnerRepoContentsPathDeleteBodyPropCommitter

    object containing information about the committer.
    """

    name: NotRequired[str]
    email: NotRequired[str]


class ReposOwnerRepoContentsPathDeleteBodyPropAuthorType(TypedDict):
    """ReposOwnerRepoContentsPathDeleteBodyPropAuthor

    object containing information about the author.
    """

    name: NotRequired[str]
    email: NotRequired[str]


__all__ = (
    "ReposOwnerRepoContentsPathDeleteBodyPropAuthorType",
    "ReposOwnerRepoContentsPathDeleteBodyPropCommitterType",
    "ReposOwnerRepoContentsPathDeleteBodyType",
)
