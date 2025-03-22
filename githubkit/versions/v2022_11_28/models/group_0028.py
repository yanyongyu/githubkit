"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class CodeSecurityConfiguration(GitHubModel):
    """CodeSecurityConfiguration

    A code security configuration
    """

    id: Missing[int] = Field(
        default=UNSET, description="The ID of the code security configuration"
    )
    name: Missing[str] = Field(
        default=UNSET,
        description="The name of the code security configuration. Must be unique within the organization.",
    )
    target_type: Missing[Literal["global", "organization", "enterprise"]] = Field(
        default=UNSET, description="The type of the code security configuration."
    )
    description: Missing[str] = Field(
        default=UNSET, description="A description of the code security configuration"
    )
    advanced_security: Missing[Literal["enabled", "disabled"]] = Field(
        default=UNSET, description="The enablement status of GitHub Advanced Security"
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
        CodeSecurityConfigurationPropDependencyGraphAutosubmitActionOptions
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
        Union[CodeSecurityConfigurationPropCodeScanningDefaultSetupOptions, None]
    ] = Field(
        default=UNSET, description="Feature options for code scanning default setup"
    )
    code_scanning_delegated_alert_dismissal: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of code scanning delegated alert dismissal",
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
    secret_scanning_delegated_bypass: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning delegated bypass",
    )
    secret_scanning_delegated_bypass_options: Missing[
        CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptions
    ] = Field(
        default=UNSET,
        description="Feature options for secret scanning delegated bypass",
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
    secret_scanning_generic_secrets: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET, description="The enablement status of Copilot secret scanning"
    )
    secret_scanning_delegated_alert_dismissal: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning delegated alert dismissal",
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
    url: Missing[str] = Field(default=UNSET, description="The URL of the configuration")
    html_url: Missing[str] = Field(
        default=UNSET, description="The URL of the configuration"
    )
    created_at: Missing[datetime] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)


class CodeSecurityConfigurationPropDependencyGraphAutosubmitActionOptions(GitHubModel):
    """CodeSecurityConfigurationPropDependencyGraphAutosubmitActionOptions

    Feature options for Automatic dependency submission
    """

    labeled_runners: Missing[bool] = Field(
        default=UNSET,
        description="Whether to use runners labeled with 'dependency-submission' or standard GitHub runners.",
    )


class CodeSecurityConfigurationPropCodeScanningDefaultSetupOptions(GitHubModel):
    """CodeSecurityConfigurationPropCodeScanningDefaultSetupOptions

    Feature options for code scanning default setup
    """

    runner_type: Missing[Union[None, Literal["standard", "labeled", "not_set"]]] = (
        Field(
            default=UNSET,
            description="Whether to use labeled runners or standard GitHub runners.",
        )
    )
    runner_label: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The label of the runner to use for code scanning when runner_type is 'labeled'.",
    )


class CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptions(GitHubModel):
    """CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptions

    Feature options for secret scanning delegated bypass
    """

    reviewers: Missing[
        list[
            CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptionsPropReviewersItems
        ]
    ] = Field(
        default=UNSET,
        description="The bypass reviewers for secret scanning delegated bypass",
    )


class CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptionsPropReviewersItems(
    GitHubModel
):
    """CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptionsPropReviewersIt
    ems
    """

    reviewer_id: int = Field(
        description="The ID of the team or role selected as a bypass reviewer"
    )
    reviewer_type: Literal["TEAM", "ROLE"] = Field(
        description="The type of the bypass reviewer"
    )


model_rebuild(CodeSecurityConfiguration)
model_rebuild(CodeSecurityConfigurationPropDependencyGraphAutosubmitActionOptions)
model_rebuild(CodeSecurityConfigurationPropCodeScanningDefaultSetupOptions)
model_rebuild(CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptions)
model_rebuild(
    CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptionsPropReviewersItems
)

__all__ = (
    "CodeSecurityConfiguration",
    "CodeSecurityConfigurationPropCodeScanningDefaultSetupOptions",
    "CodeSecurityConfigurationPropDependencyGraphAutosubmitActionOptions",
    "CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptions",
    "CodeSecurityConfigurationPropSecretScanningDelegatedBypassOptionsPropReviewersItems",
)
