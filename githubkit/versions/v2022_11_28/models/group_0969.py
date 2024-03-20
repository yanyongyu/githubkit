"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPutBodyOneof0(GitHubModel):
    """ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPutBodyOneof0

    Examples:
        {'apps': ['my-app']}
    """

    apps: List[str] = Field(
        description="The GitHub Apps that have push access to this branch. Use the slugified version of the app name. **Note**: The list of users, apps, and teams in total is limited to 100 items."
    )


model_rebuild(ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPutBodyOneof0)

__all__ = ("ReposOwnerRepoBranchesBranchProtectionRestrictionsAppsPutBodyOneof0",)
