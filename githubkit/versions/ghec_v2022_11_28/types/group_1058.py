"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class OrgsOrgPrivateRegistriesGetResponse200Type(TypedDict):
    """OrgsOrgPrivateRegistriesGetResponse200"""

    total_count: int
    configurations: list[OrgPrivateRegistryConfigurationType]


class OrgPrivateRegistryConfigurationType(TypedDict):
    """Organization private registry

    Private registry configuration for an organization
    """

    name: str
    registry_type: Literal[
        "maven_repository",
        "nuget_feed",
        "goproxy_server",
        "npm_registry",
        "rubygems_server",
        "cargo_registry",
        "composer_repository",
        "docker_registry",
        "git_source",
        "helm_registry",
        "hex_organization",
        "hex_repository",
        "pub_repository",
        "python_index",
        "terraform_registry",
    ]
    username: NotRequired[Union[str, None]]
    visibility: Literal["all", "private", "selected"]
    created_at: datetime
    updated_at: datetime


__all__ = (
    "OrgPrivateRegistryConfigurationType",
    "OrgsOrgPrivateRegistriesGetResponse200Type",
)
