"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0181 import OrganizationCustomRepositoryRole


class OrgsOrgCustomRepositoryRolesGetResponse200(GitHubModel):
    """OrgsOrgCustomRepositoryRolesGetResponse200"""

    total_count: Missing[int] = Field(
        default=UNSET, description="The number of custom roles in this organization"
    )
    custom_roles: Missing[list[OrganizationCustomRepositoryRole]] = Field(default=UNSET)


model_rebuild(OrgsOrgCustomRepositoryRolesGetResponse200)

__all__ = ("OrgsOrgCustomRepositoryRolesGetResponse200",)
