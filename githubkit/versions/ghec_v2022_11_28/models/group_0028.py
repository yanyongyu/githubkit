"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ActionsEnterprisePermissions(GitHubModel):
    """ActionsEnterprisePermissions"""

    enabled_organizations: Literal["all", "none", "selected"] = Field(
        description="The policy that controls the organizations in the enterprise that are allowed to run GitHub Actions."
    )
    selected_organizations_url: Missing[str] = Field(
        default=UNSET,
        description="The API URL to use to get or set the selected organizations that are allowed to run GitHub Actions, when `enabled_organizations` is set to `selected`.",
    )
    allowed_actions: Missing[Literal["all", "local_only", "selected"]] = Field(
        default=UNSET,
        description="The permissions policy that controls the actions and reusable workflows that are allowed to run.",
    )
    selected_actions_url: Missing[str] = Field(
        default=UNSET,
        description="The API URL to use to get or set the actions and reusable workflows that are allowed to run, when `allowed_actions` is set to `selected`.",
    )


model_rebuild(ActionsEnterprisePermissions)

__all__ = ("ActionsEnterprisePermissions",)
