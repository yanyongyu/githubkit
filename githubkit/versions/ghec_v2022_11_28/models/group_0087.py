"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser


class OrganizationCustomRepositoryRole(GitHubModel):
    """Organization Custom Repository Role

    Custom repository roles created by organization owners
    """

    id: int = Field(description="The unique identifier of the custom role.")
    name: str = Field(description="The name of the custom role.")
    description: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A short description about who this role is for or what permissions it grants.",
    )
    base_role: Literal["read", "triage", "write", "maintain"] = Field(
        description="The system role from which this role inherits permissions."
    )
    permissions: List[str] = Field(
        description="A list of additional permissions included in this role."
    )
    organization: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(OrganizationCustomRepositoryRole)

__all__ = ("OrganizationCustomRepositoryRole",)
