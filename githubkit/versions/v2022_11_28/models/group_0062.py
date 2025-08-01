"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class SecurityAndAnalysis(GitHubModel):
    """SecurityAndAnalysis"""

    advanced_security: Missing[SecurityAndAnalysisPropAdvancedSecurity] = Field(
        default=UNSET,
        description="Enable or disable GitHub Advanced Security for the repository.\n\nFor standalone Code Scanning or Secret Protection products, this parameter cannot be used.\n",
    )
    code_security: Missing[SecurityAndAnalysisPropCodeSecurity] = Field(default=UNSET)
    dependabot_security_updates: Missing[
        SecurityAndAnalysisPropDependabotSecurityUpdates
    ] = Field(
        default=UNSET,
        description="Enable or disable Dependabot security updates for the repository.",
    )
    secret_scanning: Missing[SecurityAndAnalysisPropSecretScanning] = Field(
        default=UNSET
    )
    secret_scanning_push_protection: Missing[
        SecurityAndAnalysisPropSecretScanningPushProtection
    ] = Field(default=UNSET)
    secret_scanning_non_provider_patterns: Missing[
        SecurityAndAnalysisPropSecretScanningNonProviderPatterns
    ] = Field(default=UNSET)
    secret_scanning_ai_detection: Missing[
        SecurityAndAnalysisPropSecretScanningAiDetection
    ] = Field(default=UNSET)


class SecurityAndAnalysisPropAdvancedSecurity(GitHubModel):
    """SecurityAndAnalysisPropAdvancedSecurity

    Enable or disable GitHub Advanced Security for the repository.

    For standalone Code Scanning or Secret Protection products, this parameter
    cannot be used.
    """

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


class SecurityAndAnalysisPropCodeSecurity(GitHubModel):
    """SecurityAndAnalysisPropCodeSecurity"""

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


class SecurityAndAnalysisPropDependabotSecurityUpdates(GitHubModel):
    """SecurityAndAnalysisPropDependabotSecurityUpdates

    Enable or disable Dependabot security updates for the repository.
    """

    status: Missing[Literal["enabled", "disabled"]] = Field(
        default=UNSET,
        description="The enablement status of Dependabot security updates for the repository.",
    )


class SecurityAndAnalysisPropSecretScanning(GitHubModel):
    """SecurityAndAnalysisPropSecretScanning"""

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


class SecurityAndAnalysisPropSecretScanningPushProtection(GitHubModel):
    """SecurityAndAnalysisPropSecretScanningPushProtection"""

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


class SecurityAndAnalysisPropSecretScanningNonProviderPatterns(GitHubModel):
    """SecurityAndAnalysisPropSecretScanningNonProviderPatterns"""

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


class SecurityAndAnalysisPropSecretScanningAiDetection(GitHubModel):
    """SecurityAndAnalysisPropSecretScanningAiDetection"""

    status: Missing[Literal["enabled", "disabled"]] = Field(default=UNSET)


model_rebuild(SecurityAndAnalysis)
model_rebuild(SecurityAndAnalysisPropAdvancedSecurity)
model_rebuild(SecurityAndAnalysisPropCodeSecurity)
model_rebuild(SecurityAndAnalysisPropDependabotSecurityUpdates)
model_rebuild(SecurityAndAnalysisPropSecretScanning)
model_rebuild(SecurityAndAnalysisPropSecretScanningPushProtection)
model_rebuild(SecurityAndAnalysisPropSecretScanningNonProviderPatterns)
model_rebuild(SecurityAndAnalysisPropSecretScanningAiDetection)

__all__ = (
    "SecurityAndAnalysis",
    "SecurityAndAnalysisPropAdvancedSecurity",
    "SecurityAndAnalysisPropCodeSecurity",
    "SecurityAndAnalysisPropDependabotSecurityUpdates",
    "SecurityAndAnalysisPropSecretScanning",
    "SecurityAndAnalysisPropSecretScanningAiDetection",
    "SecurityAndAnalysisPropSecretScanningNonProviderPatterns",
    "SecurityAndAnalysisPropSecretScanningPushProtection",
)
