"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0029 import CodeScanningDefaultSetupOptions


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBody(
    GitHubModel
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBody"""

    name: Missing[str] = Field(
        default=UNSET,
        description="The name of the code security configuration. Must be unique across the enterprise.",
    )
    description: Missing[str] = Field(
        max_length=255,
        default=UNSET,
        description="A description of the code security configuration",
    )
    advanced_security: Missing[Literal["enabled", "disabled"]] = Field(
        default=UNSET,
        description="The enablement status of GitHub Advanced Security. Must be set to enabled if you want to enable any GHAS settings.",
    )
    dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of Dependency Graph"
    )
    dependency_graph_autosubmit_action: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of Automatic dependency submission",
    )
    dependency_graph_autosubmit_action_options: Missing[
        EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptions
    ] = Field(
        default=UNSET, description="Feature options for Automatic dependency submission"
    )
    dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of Dependabot alerts"
    )
    dependabot_security_updates: Missing[Literal["enabled", "disabled", "not_set"]] = (
        Field(
            default=UNSET,
            description="The enablement status of Dependabot security updates",
        )
    )
    code_scanning_default_setup: Missing[Literal["enabled", "disabled", "not_set"]] = (
        Field(
            default=UNSET,
            description="The enablement status of code scanning default setup",
        )
    )
    code_scanning_default_setup_options: Missing[
        Union[CodeScanningDefaultSetupOptions, None]
    ] = Field(
        default=UNSET, description="Feature options for code scanning default setup"
    )
    secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of secret scanning"
    )
    secret_scanning_push_protection: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning push protection",
    )
    secret_scanning_validity_checks: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning validity checks",
    )
    secret_scanning_non_provider_patterns: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning non-provider patterns",
    )
    private_vulnerability_reporting: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of private vulnerability reporting",
    )
    enforcement: Missing[Literal["enforced", "unenforced"]] = Field(
        default=UNSET, description="The enforcement status for a security configuration"
    )


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptions(
    GitHubModel
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDepen
    dencyGraphAutosubmitActionOptions

    Feature options for Automatic dependency submission
    """

    labeled_runners: Missing[bool] = Field(
        default=UNSET,
        description="Whether to use runners labeled with 'dependency-submission' or standard GitHub runners.",
    )


model_rebuild(EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBody)
model_rebuild(
    EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptions
)

__all__ = (
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBody",
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptions",
)
