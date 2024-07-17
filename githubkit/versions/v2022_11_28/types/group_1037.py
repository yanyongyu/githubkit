"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPullsPullNumberReviewsPostBodyType(TypedDict):
    """ReposOwnerRepoPullsPullNumberReviewsPostBody"""

    commit_id: NotRequired[str]
    body: NotRequired[str]
    event: NotRequired[Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"]]
    comments: NotRequired[
        List[ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItemsType]
    ]


class ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItemsType(TypedDict):
    """ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItems"""

    path: str
    position: NotRequired[int]
    body: str
    line: NotRequired[int]
    side: NotRequired[str]
    start_line: NotRequired[int]
    start_side: NotRequired[str]


__all__ = (
    "ReposOwnerRepoPullsPullNumberReviewsPostBodyType",
    "ReposOwnerRepoPullsPullNumberReviewsPostBodyPropCommentsItemsType",
)
