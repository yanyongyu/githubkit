"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0252 import LinkType


class PullRequestSimplePropLinksType(TypedDict):
    """PullRequestSimplePropLinks"""

    comments: LinkType
    commits: LinkType
    statuses: LinkType
    html: LinkType
    issue: LinkType
    review_comments: LinkType
    review_comment: LinkType
    self_: LinkType


__all__ = ("PullRequestSimplePropLinksType",)
