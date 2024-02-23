"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class CustomDeploymentRuleApp(GitHubModel):
    """Custom deployment protection rule app

    A GitHub App that is providing a custom deployment protection rule.
    """

    id: int = Field(
        description="The unique identifier of the deployment protection rule integration."
    )
    slug: str = Field(
        description="The slugified name of the deployment protection rule integration."
    )
    integration_url: str = Field(
        description="The URL for the endpoint to get details about the app."
    )
    node_id: str = Field(
        description="The node ID for the deployment protection rule integration."
    )


model_rebuild(CustomDeploymentRuleApp)

__all__ = ("CustomDeploymentRuleApp",)
