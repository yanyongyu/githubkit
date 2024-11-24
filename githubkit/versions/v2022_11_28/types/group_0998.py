"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoGitTagsPostBodyType(TypedDict):
    """ReposOwnerRepoGitTagsPostBody"""

    tag: str
    message: str
    object_: str
    type: Literal["commit", "tree", "blob"]
    tagger: NotRequired[ReposOwnerRepoGitTagsPostBodyPropTaggerType]


class ReposOwnerRepoGitTagsPostBodyPropTaggerType(TypedDict):
    """ReposOwnerRepoGitTagsPostBodyPropTagger

    An object with information about the individual creating the tag.
    """

    name: str
    email: str
    date: NotRequired[datetime]


__all__ = (
    "ReposOwnerRepoGitTagsPostBodyPropTaggerType",
    "ReposOwnerRepoGitTagsPostBodyType",
)
