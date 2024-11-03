"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0385 import Meta


class ScimEnterpriseGroupResponseAllof1(GitHubModel):
    """ScimEnterpriseGroupResponseAllof1"""

    id: Missing[str] = Field(
        default=UNSET, description="The internally generated id for the group object."
    )
    members: Missing[list[ScimEnterpriseGroupResponseAllof1PropMembersItems]] = Field(
        default=UNSET, description="The security group members."
    )
    meta: Missing[Meta] = Field(
        default=UNSET,
        description="The metadata associated with the creation/updates to the user.",
    )


class ScimEnterpriseGroupResponseAllof1PropMembersItems(GitHubModel):
    """ScimEnterpriseGroupResponseAllof1PropMembersItems"""

    value: Missing[str] = Field(default=UNSET)
    ref: Missing[str] = Field(default=UNSET, alias="$ref")
    display: Missing[str] = Field(default=UNSET)


model_rebuild(ScimEnterpriseGroupResponseAllof1)
model_rebuild(ScimEnterpriseGroupResponseAllof1PropMembersItems)

__all__ = (
    "ScimEnterpriseGroupResponseAllof1",
    "ScimEnterpriseGroupResponseAllof1PropMembersItems",
)
