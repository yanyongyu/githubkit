"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import Annotated

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class GlobalAdvisoryPropCreditsItems(GitHubModel):
    """GlobalAdvisoryPropCreditsItems"""

    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
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


class GlobalAdvisory(GitHubModel):
    """GlobalAdvisory

    A GitHub Security Advisory.
    """

    ghsa_id: str = Field(description="The GitHub Security Advisory ID.")
    cve_id: Union[str, None] = Field(
        description="The Common Vulnerabilities and Exposures (CVE) ID."
    )
    url: str = Field(description="The API URL for the advisory.")
    html_url: str = Field(description="The URL for the advisory.")
    repository_advisory_url: Union[str, None] = Field(
        description="The API URL for the repository advisory."
    )
    summary: str = Field(
        max_length=1024, description="A short summary of the advisory."
    )
    description: Union[Annotated[str, Field(max_length=65535)], None] = Field(
        description="A detailed description of what the advisory entails."
    )
    type: Literal["reviewed", "unreviewed", "malware"] = Field(
        description="The type of advisory."
    )
    severity: Literal["critical", "high", "medium", "low", "unknown"] = Field(
        description="The severity of the advisory."
    )
    source_code_location: Union[str, None] = Field(
        description="The URL of the advisory's source code."
    )
    identifiers: Union[List[GlobalAdvisoryPropIdentifiersItems], None] = Field()
    references: Union[List[str], None] = Field()
    published_at: datetime = Field(
        description="The date and time of when the advisory was published, in ISO 8601 format."
    )
    updated_at: datetime = Field(
        description="The date and time of when the advisory was last updated, in ISO 8601 format."
    )
    github_reviewed_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was reviewed by GitHub, in ISO 8601 format."
    )
    nvd_published_at: Union[datetime, None] = Field(
        description="The date and time when the advisory was published in the National Vulnerability Database, in ISO 8601 format.\nThis field is only populated when the advisory is imported from the National Vulnerability Database."
    )
    withdrawn_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was withdrawn, in ISO 8601 format."
    )
    vulnerabilities: Union[List[GlobalAdvisoryPropVulnerabilitiesItems], None] = Field(
        description="The products and respective version ranges affected by the advisory."
    )
    cvss: Union[GlobalAdvisoryPropCvss, None] = Field()
    cwes: Union[List[GlobalAdvisoryPropCwesItems], None] = Field()
    credits_: Union[List[GlobalAdvisoryPropCreditsItems], None] = Field(
        alias="credits", description="The users who contributed to the advisory."
    )


class GlobalAdvisoryPropIdentifiersItems(GitHubModel):
    """GlobalAdvisoryPropIdentifiersItems"""

    type: Literal["CVE", "GHSA"] = Field(description="The type of identifier.")
    value: str = Field(description="The identifier value.")


class GlobalAdvisoryPropCvss(GitHubModel):
    """GlobalAdvisoryPropCvss"""

    vector_string: Union[str, None] = Field(description="The CVSS vector.")
    score: Union[Annotated[float, Field(le=10.0)], None] = Field(
        description="The CVSS score."
    )


class GlobalAdvisoryPropCwesItems(GitHubModel):
    """GlobalAdvisoryPropCwesItems"""

    cwe_id: str = Field(description="The Common Weakness Enumeration (CWE) identifier.")
    name: str = Field(description="The name of the CWE.")


class GlobalAdvisoryPropVulnerabilitiesItems(GitHubModel):
    """GlobalAdvisoryPropVulnerabilitiesItems"""

    package: Union[GlobalAdvisoryPropVulnerabilitiesItemsPropPackage, None] = Field(
        description="The name of the package affected by the vulnerability."
    )
    vulnerable_version_range: Union[str, None] = Field(
        description="The range of the package versions affected by the vulnerability."
    )
    first_patched_version: Union[str, None] = Field(
        description="The package version that resolve the vulnerability."
    )
    vulnerable_functions: Union[List[str], None] = Field(
        description="The functions in the package that are affected by the vulnerability."
    )


class GlobalAdvisoryPropVulnerabilitiesItemsPropPackage(GitHubModel):
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
    ] = Field(description="The package's language or package management ecosystem.")
    name: Union[str, None] = Field(
        description="The unique package name within its ecosystem."
    )


model_rebuild(GlobalAdvisoryPropCreditsItems)
model_rebuild(GlobalAdvisory)
model_rebuild(GlobalAdvisoryPropIdentifiersItems)
model_rebuild(GlobalAdvisoryPropCvss)
model_rebuild(GlobalAdvisoryPropCwesItems)
model_rebuild(GlobalAdvisoryPropVulnerabilitiesItems)
model_rebuild(GlobalAdvisoryPropVulnerabilitiesItemsPropPackage)

__all__ = (
    "GlobalAdvisoryPropCreditsItems",
    "GlobalAdvisory",
    "GlobalAdvisoryPropIdentifiersItems",
    "GlobalAdvisoryPropCvss",
    "GlobalAdvisoryPropCwesItems",
    "GlobalAdvisoryPropVulnerabilitiesItems",
    "GlobalAdvisoryPropVulnerabilitiesItemsPropPackage",
)
