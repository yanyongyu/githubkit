"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict

from .group_0003 import SimpleUserType


class RepositoryAdvisoryCreditType(TypedDict):
    """RepositoryAdvisoryCredit

    A credit given to a user for a repository security advisory.
    """

    user: SimpleUserType
    type: Literal[
        "analyst",
        "finder",
        "reporter",
        "coordinator",
        "remediation_developer",
        "remediation_reviewer",
        "remediation_verifier",
        "tool",
        "sponsor",
        "other",
    ]
    state: Literal["accepted", "declined", "pending"]


__all__ = ("RepositoryAdvisoryCreditType",)
