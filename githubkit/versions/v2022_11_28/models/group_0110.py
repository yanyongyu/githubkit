"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class PackageVersion(GitHubModel):
    """Package Version

    A version of a software package
    """

    id: int = Field(description="Unique identifier of the package version.")
    name: str = Field(description="The name of the package version.")
    url: str = Field()
    package_html_url: str = Field()
    html_url: Missing[str] = Field(default=UNSET)
    license_: Missing[str] = Field(default=UNSET, alias="license")
    description: Missing[str] = Field(default=UNSET)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    deleted_at: Missing[datetime] = Field(default=UNSET)
    metadata: Missing[PackageVersionPropMetadata] = Field(
        default=UNSET, title="Package Version Metadata"
    )


class PackageVersionPropMetadata(GitHubModel):
    """Package Version Metadata"""

    package_type: Literal[
        "npm", "maven", "rubygems", "docker", "nuget", "container"
    ] = Field()
    container: Missing[PackageVersionPropMetadataPropContainer] = Field(
        default=UNSET, title="Container Metadata"
    )
    docker: Missing[PackageVersionPropMetadataPropDocker] = Field(
        default=UNSET, title="Docker Metadata"
    )


class PackageVersionPropMetadataPropContainer(GitHubModel):
    """Container Metadata"""

    tags: list[str] = Field()


class PackageVersionPropMetadataPropDocker(GitHubModel):
    """Docker Metadata"""

    tag: Missing[list[str]] = Field(default=UNSET)


model_rebuild(PackageVersion)
model_rebuild(PackageVersionPropMetadata)
model_rebuild(PackageVersionPropMetadataPropContainer)
model_rebuild(PackageVersionPropMetadataPropDocker)

__all__ = (
    "PackageVersion",
    "PackageVersionPropMetadata",
    "PackageVersionPropMetadataPropContainer",
    "PackageVersionPropMetadataPropDocker",
)
