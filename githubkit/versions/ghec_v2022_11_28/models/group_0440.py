"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Group(GitHubModel):
    """Group"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]] = Field(
        description="The URIs that are used to indicate the namespaces of the SCIM schemas."
    )
    external_id: str = Field(
        alias="externalId",
        description="A unique identifier for the resource as defined by the provisioning client.",
    )
    display_name: str = Field(
        alias="displayName", description="A human-readable name for a security group."
    )
    members: list[GroupPropMembersItems] = Field(description="The group members.")


class GroupPropMembersItems(GitHubModel):
    """GroupPropMembersItems"""

    value: str = Field(description="The local unique identifier for the member")
    display_name: str = Field(
        alias="displayName", description="The display name associated with the member"
    )


model_rebuild(Group)
model_rebuild(GroupPropMembersItems)

__all__ = (
    "Group",
    "GroupPropMembersItems",
)
