"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsCacheUsageByRepositoryGetResponse200(GitHubModel):
    """OrgsOrgActionsCacheUsageByRepositoryGetResponse200"""

    total_count: int = Field()
    repository_cache_usages: list[ActionsCacheUsageByRepository] = Field()


class ActionsCacheUsageByRepository(GitHubModel):
    """Actions Cache Usage by repository

    GitHub Actions Cache Usage by repository.
    """

    full_name: str = Field(
        description="The repository owner and name for the cache usage being shown."
    )
    active_caches_size_in_bytes: int = Field(
        description="The sum of the size in bytes of all the active cache items in the repository."
    )
    active_caches_count: int = Field(
        description="The number of active caches in the repository."
    )


model_rebuild(OrgsOrgActionsCacheUsageByRepositoryGetResponse200)
model_rebuild(ActionsCacheUsageByRepository)

__all__ = (
    "ActionsCacheUsageByRepository",
    "OrgsOrgActionsCacheUsageByRepositoryGetResponse200",
)
