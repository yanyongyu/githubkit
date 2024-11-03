"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBody(GitHubModel):
    """ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBody"""

    strict: Missing[bool] = Field(
        default=UNSET, description="Require branches to be up to date before merging."
    )
    contexts: Missing[list[str]] = Field(
        default=UNSET,
        description="**Closing down notice**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use `checks` instead of `contexts` for more fine-grained control.",
    )
    checks: Missing[
        list[
            ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBodyPropChecksItems
        ]
    ] = Field(
        default=UNSET,
        description="The list of status checks to require in order to merge into this branch.",
    )


class ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBodyPropChecksItems(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBodyPropChecksIte
    ms
    """

    context: str = Field(description="The name of the required check")
    app_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the GitHub App that must provide this check. Omit this field to automatically select the GitHub App that has recently provided this check, or any app if it was not set by a GitHub App. Pass -1 to explicitly allow any app to set the status.",
    )


model_rebuild(ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBody)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBodyPropChecksItems
)

__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBody",
    "ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksPatchBodyPropChecksItems",
)
