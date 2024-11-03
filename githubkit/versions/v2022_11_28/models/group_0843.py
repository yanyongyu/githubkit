"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgDependabotSecretsGetResponse200(GitHubModel):
    """OrgsOrgDependabotSecretsGetResponse200"""

    total_count: int = Field()
    secrets: list[OrganizationDependabotSecret] = Field()


class OrganizationDependabotSecret(GitHubModel):
    """Dependabot Secret for an Organization

    Secrets for GitHub Dependabot for an organization.
    """

    name: str = Field(description="The name of the secret.")
    created_at: datetime = Field()
    updated_at: datetime = Field()
    visibility: Literal["all", "private", "selected"] = Field(
        description="Visibility of a secret"
    )
    selected_repositories_url: Missing[str] = Field(default=UNSET)


model_rebuild(OrgsOrgDependabotSecretsGetResponse200)
model_rebuild(OrganizationDependabotSecret)

__all__ = (
    "OrgsOrgDependabotSecretsGetResponse200",
    "OrganizationDependabotSecret",
)
