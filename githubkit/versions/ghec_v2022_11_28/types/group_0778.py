"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import CvssSeveritiesType


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType
    cvss_severities: NotRequired[Union[CvssSeveritiesType, None]]
    cwes: list[WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType]
    description: str
    ghsa_id: str
    identifiers: list[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType
    ]
    published_at: str
    references: list[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType
    ]
    severity: str
    summary: str
    updated_at: str
    vulnerabilities: list[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType
    ]
    withdrawn_at: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvss"""

    score: float
    vector_string: Union[str, None]


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType(TypedDict):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItems"""

    type: str
    value: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItems"""

    url: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType,
        None,
    ]
    package: WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType
    severity: str
    vulnerable_version_range: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    FirstPatchedVersion
    """

    identifier: str


class WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType(
    TypedDict
):
    """WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsProp
    Package
    """

    ecosystem: str
    name: str


__all__ = (
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCvssType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropCwesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropIdentifiersItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropReferencesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersionType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsPropPackageType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryPropVulnerabilitiesItemsType",
    "WebhookSecurityAdvisoryWithdrawnPropSecurityAdvisoryType",
)
