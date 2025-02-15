"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0029 import CodeScanningDefaultSetupOptionsType


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyType(
    TypedDict
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBody"""

    name: NotRequired[str]
    description: NotRequired[str]
    advanced_security: NotRequired[Literal["enabled", "disabled"]]
    dependency_graph: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependency_graph_autosubmit_action: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    dependency_graph_autosubmit_action_options: NotRequired[
        EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType
    ]
    dependabot_alerts: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_security_updates: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup_options: NotRequired[
        Union[CodeScanningDefaultSetupOptionsType, None]
    ]
    secret_scanning: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning_push_protection: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_validity_checks: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_non_provider_patterns: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    private_vulnerability_reporting: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    enforcement: NotRequired[Literal["enforced", "unenforced"]]


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType(
    TypedDict
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDepen
    dencyGraphAutosubmitActionOptions

    Feature options for Automatic dependency submission
    """

    labeled_runners: NotRequired[bool]


__all__ = (
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType",
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyType",
)
