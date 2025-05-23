"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict


class PackageVersionType(TypedDict):
    """Package Version

    A version of a software package
    """

    id: int
    name: str
    url: str
    package_html_url: str
    html_url: NotRequired[str]
    license_: NotRequired[str]
    description: NotRequired[str]
    created_at: datetime
    updated_at: datetime
    deleted_at: NotRequired[datetime]
    metadata: NotRequired[PackageVersionPropMetadataType]


class PackageVersionPropMetadataType(TypedDict):
    """Package Version Metadata"""

    package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"]
    container: NotRequired[PackageVersionPropMetadataPropContainerType]
    docker: NotRequired[PackageVersionPropMetadataPropDockerType]


class PackageVersionPropMetadataPropContainerType(TypedDict):
    """Container Metadata"""

    tags: list[str]


class PackageVersionPropMetadataPropDockerType(TypedDict):
    """Docker Metadata"""

    tag: NotRequired[list[str]]


__all__ = (
    "PackageVersionPropMetadataPropContainerType",
    "PackageVersionPropMetadataPropDockerType",
    "PackageVersionPropMetadataType",
    "PackageVersionType",
)
