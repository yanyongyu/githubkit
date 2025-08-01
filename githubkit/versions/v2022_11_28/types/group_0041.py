"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class SecretScanningLocationDiscussionBodyType(TypedDict):
    """SecretScanningLocationDiscussionBody

    Represents a 'discussion_body' secret scanning location type. This location type
    shows that a secret was detected in the body of a discussion.
    """

    discussion_body_url: str


class SecretScanningLocationPullRequestCommentType(TypedDict):
    """SecretScanningLocationPullRequestComment

    Represents a 'pull_request_comment' secret scanning location type. This location
    type shows that a secret was detected in a comment on a pull request.
    """

    pull_request_comment_url: str


__all__ = (
    "SecretScanningLocationDiscussionBodyType",
    "SecretScanningLocationPullRequestCommentType",
)
