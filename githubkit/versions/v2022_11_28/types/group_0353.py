"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0003 import SimpleUserType
from .group_0086 import TeamType


class PullRequestReviewRequestType(TypedDict):
    """Pull Request Review Request

    Pull Request Review Request
    """

    users: list[SimpleUserType]
    teams: list[TeamType]


__all__ = ("PullRequestReviewRequestType",)
