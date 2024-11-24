"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgsOrgCodeSecurityConfigurationsDetachDeleteBody(GitHubModel):
    """OrgsOrgCodeSecurityConfigurationsDetachDeleteBody"""

    selected_repository_ids: Missing[list[int]] = Field(
        default=UNSET,
        description="An array of repository IDs to detach from configurations.",
    )


model_rebuild(OrgsOrgCodeSecurityConfigurationsDetachDeleteBody)

__all__ = ("OrgsOrgCodeSecurityConfigurationsDetachDeleteBody",)
