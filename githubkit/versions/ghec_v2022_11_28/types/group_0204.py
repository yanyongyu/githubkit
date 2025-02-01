"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0001 import CvssSeveritiesType
from .group_0003 import SimpleUserType
from .group_0065 import TeamType
from .group_0203 import RepositoryAdvisoryCreditType


class RepositoryAdvisoryType(TypedDict):
    """RepositoryAdvisory

    A repository security advisory.
    """

    ghsa_id: str
    cve_id: Union[str, None]
    url: str
    html_url: str
    summary: str
    description: Union[str, None]
    severity: Union[None, Literal["critical", "high", "medium", "low"]]
    author: None
    publisher: None
    identifiers: list[RepositoryAdvisoryPropIdentifiersItemsType]
    state: Literal["published", "closed", "withdrawn", "draft", "triage"]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    published_at: Union[datetime, None]
    closed_at: Union[datetime, None]
    withdrawn_at: Union[datetime, None]
    submission: Union[RepositoryAdvisoryPropSubmissionType, None]
    vulnerabilities: Union[list[RepositoryAdvisoryVulnerabilityType], None]
    cvss: Union[RepositoryAdvisoryPropCvssType, None]
    cvss_severities: NotRequired[Union[CvssSeveritiesType, None]]
    cwes: Union[list[RepositoryAdvisoryPropCwesItemsType], None]
    cwe_ids: Union[list[str], None]
    credits_: Union[list[RepositoryAdvisoryPropCreditsItemsType], None]
    credits_detailed: Union[list[RepositoryAdvisoryCreditType], None]
    collaborating_users: Union[list[SimpleUserType], None]
    collaborating_teams: Union[list[TeamType], None]
    private_fork: None


class RepositoryAdvisoryPropIdentifiersItemsType(TypedDict):
    """RepositoryAdvisoryPropIdentifiersItems"""

    type: Literal["CVE", "GHSA"]
    value: str


class RepositoryAdvisoryPropSubmissionType(TypedDict):
    """RepositoryAdvisoryPropSubmission"""

    accepted: bool


class RepositoryAdvisoryPropCvssType(TypedDict):
    """RepositoryAdvisoryPropCvss"""

    vector_string: Union[str, None]
    score: Union[float, None]


class RepositoryAdvisoryPropCwesItemsType(TypedDict):
    """RepositoryAdvisoryPropCwesItems"""

    cwe_id: str
    name: str


class RepositoryAdvisoryPropCreditsItemsType(TypedDict):
    """RepositoryAdvisoryPropCreditsItems"""

    login: NotRequired[str]
    type: NotRequired[
        Literal[
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
    ]


class RepositoryAdvisoryVulnerabilityType(TypedDict):
    """RepositoryAdvisoryVulnerability

    A product affected by the vulnerability detailed in a repository security
    advisory.
    """

    package: Union[RepositoryAdvisoryVulnerabilityPropPackageType, None]
    vulnerable_version_range: Union[str, None]
    patched_versions: Union[str, None]
    vulnerable_functions: Union[list[str], None]


class RepositoryAdvisoryVulnerabilityPropPackageType(TypedDict):
    """RepositoryAdvisoryVulnerabilityPropPackage

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
    "RepositoryAdvisoryPropCreditsItemsType",
    "RepositoryAdvisoryPropCvssType",
    "RepositoryAdvisoryPropCwesItemsType",
    "RepositoryAdvisoryPropIdentifiersItemsType",
    "RepositoryAdvisoryPropSubmissionType",
    "RepositoryAdvisoryType",
    "RepositoryAdvisoryVulnerabilityPropPackageType",
    "RepositoryAdvisoryVulnerabilityType",
)
