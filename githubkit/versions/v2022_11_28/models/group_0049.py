"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class SecurityAndAnalysis(GitHubModel):
    """SecurityAndAnalysis"""

    advanced_security: Missing[SecurityAndAnalysisPropAdvancedSecurity] = Field(
        default=UNSET
    )
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


class SecurityAndAnalysisPropAdvancedSecurity(GitHubModel):
    """SecurityAndAnalysisPropAdvancedSecurity"""

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


model_rebuild(SecurityAndAnalysis)
model_rebuild(SecurityAndAnalysisPropAdvancedSecurity)
model_rebuild(SecurityAndAnalysisPropDependabotSecurityUpdates)
model_rebuild(SecurityAndAnalysisPropSecretScanning)
model_rebuild(SecurityAndAnalysisPropSecretScanningPushProtection)

__all__ = (
    "SecurityAndAnalysis",
    "SecurityAndAnalysisPropAdvancedSecurity",
    "SecurityAndAnalysisPropDependabotSecurityUpdates",
    "SecurityAndAnalysisPropSecretScanning",
    "SecurityAndAnalysisPropSecretScanningPushProtection",
)
