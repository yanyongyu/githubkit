"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class ApiOverviewType(TypedDict):
    """Api Overview

    Api Overview
    """

    verifiable_password_authentication: bool
    ssh_key_fingerprints: NotRequired[ApiOverviewPropSshKeyFingerprintsType]
    ssh_keys: NotRequired[list[str]]
    hooks: NotRequired[list[str]]
    github_enterprise_importer: NotRequired[list[str]]
    web: NotRequired[list[str]]
    api: NotRequired[list[str]]
    git: NotRequired[list[str]]
    packages: NotRequired[list[str]]
    pages: NotRequired[list[str]]
    importer: NotRequired[list[str]]
    actions: NotRequired[list[str]]
    actions_macos: NotRequired[list[str]]
    codespaces: NotRequired[list[str]]
    dependabot: NotRequired[list[str]]
    copilot: NotRequired[list[str]]
    domains: NotRequired[ApiOverviewPropDomainsType]


class ApiOverviewPropSshKeyFingerprintsType(TypedDict):
    """ApiOverviewPropSshKeyFingerprints"""

    sha256_rsa: NotRequired[str]
    sha256_dsa: NotRequired[str]
    sha256_ecdsa: NotRequired[str]
    sha256_ed25519: NotRequired[str]


class ApiOverviewPropDomainsType(TypedDict):
    """ApiOverviewPropDomains"""

    website: NotRequired[list[str]]
    codespaces: NotRequired[list[str]]
    copilot: NotRequired[list[str]]
    packages: NotRequired[list[str]]
    actions: NotRequired[list[str]]
    artifact_attestations: NotRequired[
        ApiOverviewPropDomainsPropArtifactAttestationsType
    ]


class ApiOverviewPropDomainsPropArtifactAttestationsType(TypedDict):
    """ApiOverviewPropDomainsPropArtifactAttestations"""

    trust_domain: NotRequired[str]
    services: NotRequired[list[str]]


__all__ = (
    "ApiOverviewPropDomainsPropArtifactAttestationsType",
    "ApiOverviewPropDomainsType",
    "ApiOverviewPropSshKeyFingerprintsType",
    "ApiOverviewType",
)
