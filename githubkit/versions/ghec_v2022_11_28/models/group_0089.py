"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ApiOverview(GitHubModel):
    """Api Overview

    Api Overview
    """

    verifiable_password_authentication: bool = Field()
    ssh_key_fingerprints: Missing[ApiOverviewPropSshKeyFingerprints] = Field(
        default=UNSET
    )
    ssh_keys: Missing[list[str]] = Field(default=UNSET)
    hooks: Missing[list[str]] = Field(default=UNSET)
    github_enterprise_importer: Missing[list[str]] = Field(default=UNSET)
    web: Missing[list[str]] = Field(default=UNSET)
    api: Missing[list[str]] = Field(default=UNSET)
    git: Missing[list[str]] = Field(default=UNSET)
    packages: Missing[list[str]] = Field(default=UNSET)
    pages: Missing[list[str]] = Field(default=UNSET)
    importer: Missing[list[str]] = Field(default=UNSET)
    actions: Missing[list[str]] = Field(default=UNSET)
    actions_macos: Missing[list[str]] = Field(default=UNSET)
    codespaces: Missing[list[str]] = Field(default=UNSET)
    dependabot: Missing[list[str]] = Field(default=UNSET)
    copilot: Missing[list[str]] = Field(default=UNSET)
    domains: Missing[ApiOverviewPropDomains] = Field(default=UNSET)


class ApiOverviewPropSshKeyFingerprints(GitHubModel):
    """ApiOverviewPropSshKeyFingerprints"""

    sha256_rsa: Missing[str] = Field(default=UNSET, alias="SHA256_RSA")
    sha256_dsa: Missing[str] = Field(default=UNSET, alias="SHA256_DSA")
    sha256_ecdsa: Missing[str] = Field(default=UNSET, alias="SHA256_ECDSA")
    sha256_ed25519: Missing[str] = Field(default=UNSET, alias="SHA256_ED25519")


class ApiOverviewPropDomains(GitHubModel):
    """ApiOverviewPropDomains"""

    website: Missing[list[str]] = Field(default=UNSET)
    codespaces: Missing[list[str]] = Field(default=UNSET)
    copilot: Missing[list[str]] = Field(default=UNSET)
    packages: Missing[list[str]] = Field(default=UNSET)
    actions: Missing[list[str]] = Field(default=UNSET)
    artifact_attestations: Missing[ApiOverviewPropDomainsPropArtifactAttestations] = (
        Field(default=UNSET)
    )


class ApiOverviewPropDomainsPropArtifactAttestations(GitHubModel):
    """ApiOverviewPropDomainsPropArtifactAttestations"""

    trust_domain: Missing[str] = Field(default=UNSET)
    services: Missing[list[str]] = Field(default=UNSET)


model_rebuild(ApiOverview)
model_rebuild(ApiOverviewPropSshKeyFingerprints)
model_rebuild(ApiOverviewPropDomains)
model_rebuild(ApiOverviewPropDomainsPropArtifactAttestations)

__all__ = (
    "ApiOverview",
    "ApiOverviewPropDomains",
    "ApiOverviewPropDomainsPropArtifactAttestations",
    "ApiOverviewPropSshKeyFingerprints",
)
