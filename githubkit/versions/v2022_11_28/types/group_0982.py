"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsPutBodyOneof0Type(
    TypedDict
):
    """ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsPutBodyOneof0

    Examples:
        {'teams': ['justice-league']}
    """

    teams: list[str]


__all__ = ("ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsPutBodyOneof0Type",)
