"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict


class DependencyGraphDiffItemsType(TypedDict):
    """DependencyGraphDiffItems"""

    change_type: Literal["added", "removed"]
    manifest: str
    ecosystem: str
    name: str
    version: str
    package_url: Union[str, None]
    license_: Union[str, None]
    source_repository_url: Union[str, None]
    vulnerabilities: list[DependencyGraphDiffItemsPropVulnerabilitiesItemsType]
    scope: Literal["unknown", "runtime", "development"]


class DependencyGraphDiffItemsPropVulnerabilitiesItemsType(TypedDict):
    """DependencyGraphDiffItemsPropVulnerabilitiesItems"""

    severity: str
    advisory_ghsa_id: str
    advisory_summary: str
    advisory_url: str


__all__ = (
    "DependencyGraphDiffItemsType",
    "DependencyGraphDiffItemsPropVulnerabilitiesItemsType",
)
