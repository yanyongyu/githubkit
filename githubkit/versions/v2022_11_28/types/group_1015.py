"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0240 import CustomDeploymentRuleAppType


class ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetRespons
    e200
    """

    total_count: NotRequired[int]
    available_custom_deployment_protection_rule_integrations: NotRequired[
        List[CustomDeploymentRuleAppType]
    ]


__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetResponse200Type",
)
