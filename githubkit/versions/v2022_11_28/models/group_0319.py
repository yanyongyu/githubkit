"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryAdvisoryUpdate(GitHubModel):
    """RepositoryAdvisoryUpdate"""

    summary: Missing[str] = Field(
        max_length=1024, default=UNSET, description="A short summary of the advisory."
    )
    description: Missing[str] = Field(
        max_length=65535,
        default=UNSET,
        description="A detailed description of what the advisory impacts.",
    )
    cve_id: Missing[Union[str, None]] = Field(
        default=UNSET, description="The Common Vulnerabilities and Exposures (CVE) ID."
    )
    vulnerabilities: Missing[List[RepositoryAdvisoryUpdatePropVulnerabilitiesItems]] = (
        Field(
            default=UNSET,
            description="A product affected by the vulnerability detailed in a repository security advisory.",
        )
    )
    cwe_ids: Missing[Union[List[str], None]] = Field(
        default=UNSET, description="A list of Common Weakness Enumeration (CWE) IDs."
    )
    credits_: Missing[Union[List[RepositoryAdvisoryUpdatePropCreditsItems], None]] = (
        Field(
            default=UNSET,
            alias="credits",
            description="A list of users receiving credit for their participation in the security advisory.",
        )
    )
    severity: Missing[Union[None, Literal["critical", "high", "medium", "low"]]] = (
        Field(
            default=UNSET,
            description="The severity of the advisory. You must choose between setting this field or `cvss_vector_string`.",
        )
    )
    cvss_vector_string: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or `severity`.",
    )
    state: Missing[Literal["published", "closed", "draft"]] = Field(
        default=UNSET, description="The state of the advisory."
    )
    collaborating_users: Missing[Union[List[str], None]] = Field(
        default=UNSET,
        description="A list of usernames who have been granted write access to the advisory.",
    )
    collaborating_teams: Missing[Union[List[str], None]] = Field(
        default=UNSET,
        description="A list of team slugs which have been granted write access to the advisory.",
    )


class RepositoryAdvisoryUpdatePropCreditsItems(GitHubModel):
    """RepositoryAdvisoryUpdatePropCreditsItems"""

    login: str = Field(description="The username of the user credited.")
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
    ] = Field(description="The type of credit the user is receiving.")


class RepositoryAdvisoryUpdatePropVulnerabilitiesItems(GitHubModel):
    """RepositoryAdvisoryUpdatePropVulnerabilitiesItems"""

    package: RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage = Field(
        description="The name of the package affected by the vulnerability."
    )
    vulnerable_version_range: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The range of the package versions affected by the vulnerability.",
    )
    patched_versions: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The package version(s) that resolve the vulnerability.",
    )
    vulnerable_functions: Missing[Union[List[str], None]] = Field(
        default=UNSET, description="The functions in the package that are affected."
    )


class RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage(GitHubModel):
    """RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage

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
    ] = Field(description="The package's language or package management ecosystem.")
    name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The unique package name within its ecosystem."
    )


model_rebuild(RepositoryAdvisoryUpdate)
model_rebuild(RepositoryAdvisoryUpdatePropCreditsItems)
model_rebuild(RepositoryAdvisoryUpdatePropVulnerabilitiesItems)
model_rebuild(RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage)

__all__ = (
    "RepositoryAdvisoryUpdate",
    "RepositoryAdvisoryUpdatePropCreditsItems",
    "RepositoryAdvisoryUpdatePropVulnerabilitiesItems",
    "RepositoryAdvisoryUpdatePropVulnerabilitiesItemsPropPackage",
)
