"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0240 import CustomDeploymentRuleApp


class DeploymentProtectionRule(GitHubModel):
    """Deployment protection rule

    Deployment protection rule
    """

    id: int = Field(
        description="The unique identifier for the deployment protection rule."
    )
    node_id: str = Field(description="The node ID for the deployment protection rule.")
    enabled: bool = Field(
        description="Whether the deployment protection rule is enabled for the environment."
    )
    app: CustomDeploymentRuleApp = Field(
        title="Custom deployment protection rule app",
        description="A GitHub App that is providing a custom deployment protection rule.",
    )


class ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200(
    GitHubModel
):
    """ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200

    Examples:
        {'$ref': '#/components/examples/deployment-protection-rules'}
    """

    total_count: Missing[int] = Field(
        default=UNSET,
        description="The number of enabled custom deployment protection rules for this environment",
    )
    custom_deployment_protection_rules: Missing[List[DeploymentProtectionRule]] = Field(
        default=UNSET
    )


model_rebuild(DeploymentProtectionRule)
model_rebuild(
    ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200
)

__all__ = (
    "DeploymentProtectionRule",
    "ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200",
)
