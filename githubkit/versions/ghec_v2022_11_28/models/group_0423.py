"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0421 import UserEmailsResponseItems, UserNameResponse
from .group_0422 import UserRoleItems


class UserResponse(GitHubModel):
    """UserResponse"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]] = Field(
        description="The URIs that are used to indicate the namespaces of the SCIM schemas."
    )
    external_id: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="externalId",
        description="A unique identifier for the resource as defined by the provisioning client.",
    )
    active: bool = Field(description="Whether the user active in the IdP.")
    user_name: Missing[str] = Field(
        default=UNSET, alias="userName", description="The username for the user."
    )
    name: Missing[UserNameResponse] = Field(default=UNSET)
    display_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="displayName",
        description="A human-readable name for the user.",
    )
    emails: list[UserEmailsResponseItems] = Field(
        description="The emails for the user."
    )
    roles: Missing[list[UserRoleItems]] = Field(
        default=UNSET, description="The roles assigned to the user."
    )


model_rebuild(UserResponse)

__all__ = ("UserResponse",)
