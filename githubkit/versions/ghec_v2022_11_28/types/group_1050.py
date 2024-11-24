"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoContentsPathPutBodyType(TypedDict):
    """ReposOwnerRepoContentsPathPutBody"""

    message: str
    content: str
    sha: NotRequired[str]
    branch: NotRequired[str]
    committer: NotRequired[ReposOwnerRepoContentsPathPutBodyPropCommitterType]
    author: NotRequired[ReposOwnerRepoContentsPathPutBodyPropAuthorType]


class ReposOwnerRepoContentsPathPutBodyPropCommitterType(TypedDict):
    """ReposOwnerRepoContentsPathPutBodyPropCommitter

    The person that committed the file. Default: the authenticated user.
    """

    name: str
    email: str
    date: NotRequired[str]


class ReposOwnerRepoContentsPathPutBodyPropAuthorType(TypedDict):
    """ReposOwnerRepoContentsPathPutBodyPropAuthor

    The author of the file. Default: The `committer` or the authenticated user if
    you omit `committer`.
    """

    name: str
    email: str
    date: NotRequired[str]


__all__ = (
    "ReposOwnerRepoContentsPathPutBodyPropAuthorType",
    "ReposOwnerRepoContentsPathPutBodyPropCommitterType",
    "ReposOwnerRepoContentsPathPutBodyType",
)
