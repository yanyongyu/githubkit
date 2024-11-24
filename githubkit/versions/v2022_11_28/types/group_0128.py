"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0129 import RepositoryRuleRequiredDeploymentsPropParametersType


class RepositoryRuleRequiredDeploymentsType(TypedDict):
    """required_deployments

    Choose which environments must be successfully deployed to before refs can be
    pushed into a ref that matches this rule.
    """

    type: Literal["required_deployments"]
    parameters: NotRequired[RepositoryRuleRequiredDeploymentsPropParametersType]


__all__ = ("RepositoryRuleRequiredDeploymentsType",)
