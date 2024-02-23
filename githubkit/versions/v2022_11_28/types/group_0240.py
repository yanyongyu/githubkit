"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0239 import CustomDeploymentRuleAppType


class DeploymentProtectionRuleType(TypedDict):
    """Deployment protection rule

    Deployment protection rule
    """

    id: int
    node_id: str
    enabled: bool
    app: CustomDeploymentRuleAppType


class ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200

    Examples:
        {'$ref': '#/components/examples/deployment-protection-rules'}
    """

    total_count: NotRequired[int]
    custom_deployment_protection_rules: NotRequired[List[DeploymentProtectionRuleType]]


__all__ = (
    "DeploymentProtectionRuleType",
    "ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesGetResponse200Type",
)
