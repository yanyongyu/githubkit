"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class RepositoryAdvisoryCreateType(TypedDict):
    """RepositoryAdvisoryCreate"""

    summary: str
    description: str
    cve_id: NotRequired[Union[str, None]]
    vulnerabilities: list[RepositoryAdvisoryCreatePropVulnerabilitiesItemsType]
    cwe_ids: NotRequired[Union[list[str], None]]
    credits_: NotRequired[
        Union[list[RepositoryAdvisoryCreatePropCreditsItemsType], None]
    ]
    severity: NotRequired[Union[None, Literal["critical", "high", "medium", "low"]]]
    cvss_vector_string: NotRequired[Union[str, None]]
    start_private_fork: NotRequired[bool]


class RepositoryAdvisoryCreatePropCreditsItemsType(TypedDict):
    """RepositoryAdvisoryCreatePropCreditsItems"""

    login: str
    type: Literal[
        "analyst",
        "finder",
        "reporter",
        "coordinator",
        "remediation_developer",
        "remediation_reviewer",
        "remediation_verifier",
        "tool",
        "sponsor",
        "other",
    ]


class RepositoryAdvisoryCreatePropVulnerabilitiesItemsType(TypedDict):
    """RepositoryAdvisoryCreatePropVulnerabilitiesItems"""

    package: RepositoryAdvisoryCreatePropVulnerabilitiesItemsPropPackageType
    vulnerable_version_range: NotRequired[Union[str, None]]
    patched_versions: NotRequired[Union[str, None]]
    vulnerable_functions: NotRequired[Union[list[str], None]]


class RepositoryAdvisoryCreatePropVulnerabilitiesItemsPropPackageType(TypedDict):
    """RepositoryAdvisoryCreatePropVulnerabilitiesItemsPropPackage

    The name of the package affected by the vulnerability.
    """

    ecosystem: Literal[
        "rubygems",
        "npm",
        "pip",
        "maven",
        "nuget",
        "composer",
        "go",
        "rust",
        "erlang",
        "actions",
        "pub",
        "other",
        "swift",
    ]
    name: NotRequired[Union[str, None]]


__all__ = (
    "RepositoryAdvisoryCreatePropCreditsItemsType",
    "RepositoryAdvisoryCreatePropVulnerabilitiesItemsPropPackageType",
    "RepositoryAdvisoryCreatePropVulnerabilitiesItemsType",
    "RepositoryAdvisoryCreateType",
)
