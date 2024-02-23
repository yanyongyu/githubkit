"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0

    Examples:
        {'contexts': ['contexts']}
    """

    contexts: List[str] = Field(description="The name of the status checks")


model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0
)

__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0",
)
