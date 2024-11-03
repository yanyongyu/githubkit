"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCodespacesSecretsSecretNameRepositoriesPutBody(GitHubModel):
    """OrgsOrgCodespacesSecretsSecretNameRepositoriesPutBody"""

    selected_repository_ids: list[int] = Field(
        description="An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the `visibility` is set to `selected`. You can add and remove individual repositories using the [Set selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#set-selected-repositories-for-an-organization-secret) and [Remove selected repository from an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#remove-selected-repository-from-an-organization-secret) endpoints."
    )


model_rebuild(OrgsOrgCodespacesSecretsSecretNameRepositoriesPutBody)

__all__ = ("OrgsOrgCodespacesSecretsSecretNameRepositoriesPutBody",)
