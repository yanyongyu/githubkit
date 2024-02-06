"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict

from .group_0001 import SimpleUserType


class GlobalAdvisoryPropCreditsItemsType(TypedDict):
    """GlobalAdvisoryPropCreditsItems"""

    user: SimpleUserType
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


class GlobalAdvisoryType(TypedDict):
    """GlobalAdvisory

    A GitHub Security Advisory.
    """

    ghsa_id: str
    cve_id: Union[str, None]
    url: str
    html_url: str
    repository_advisory_url: Union[str, None]
    summary: str
    description: Union[str, None]
    type: Literal["reviewed", "unreviewed", "malware"]
    severity: Literal["critical", "high", "medium", "low", "unknown"]
    source_code_location: Union[str, None]
    identifiers: Union[List[GlobalAdvisoryPropIdentifiersItemsType], None]
    references: Union[List[str], None]
    published_at: datetime
    updated_at: datetime
    github_reviewed_at: Union[datetime, None]
    nvd_published_at: Union[datetime, None]
    withdrawn_at: Union[datetime, None]
    vulnerabilities: Union[List[GlobalAdvisoryPropVulnerabilitiesItemsType], None]
    cvss: Union[GlobalAdvisoryPropCvssType, None]
    cwes: Union[List[GlobalAdvisoryPropCwesItemsType], None]
    credits_: Union[List[GlobalAdvisoryPropCreditsItemsType], None]


class GlobalAdvisoryPropIdentifiersItemsType(TypedDict):
    """GlobalAdvisoryPropIdentifiersItems"""

    type: Literal["CVE", "GHSA"]
    value: str


class GlobalAdvisoryPropCvssType(TypedDict):
    """GlobalAdvisoryPropCvss"""

    vector_string: Union[str, None]
    score: Union[float, None]


class GlobalAdvisoryPropCwesItemsType(TypedDict):
    """GlobalAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class GlobalAdvisoryPropVulnerabilitiesItemsType(TypedDict):
    """GlobalAdvisoryPropVulnerabilitiesItems"""

    package: Union[GlobalAdvisoryPropVulnerabilitiesItemsPropPackageType, None]
    vulnerable_version_range: Union[str, None]
    first_patched_version: Union[str, None]
    vulnerable_functions: Union[List[str], None]


class GlobalAdvisoryPropVulnerabilitiesItemsPropPackageType(TypedDict):
    """GlobalAdvisoryPropVulnerabilitiesItemsPropPackage

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
    name: Union[str, None]


__all__ = (
    "GlobalAdvisoryPropCreditsItemsType",
    "GlobalAdvisoryType",
    "GlobalAdvisoryPropIdentifiersItemsType",
    "GlobalAdvisoryPropCvssType",
    "GlobalAdvisoryPropCwesItemsType",
    "GlobalAdvisoryPropVulnerabilitiesItemsType",
    "GlobalAdvisoryPropVulnerabilitiesItemsPropPackageType",
)
