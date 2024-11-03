"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0019 import Repository


class AuthenticationToken(GitHubModel):
    """Authentication Token

    Authentication Token
    """

    token: str = Field(description="The token used for authentication")
    expires_at: datetime = Field(description="The time this token expires")
    permissions: Missing[AuthenticationTokenPropPermissions] = Field(default=UNSET)
    repositories: Missing[list[Repository]] = Field(
        default=UNSET, description="The repositories this token has access to"
    )
    single_file: Missing[Union[str, None]] = Field(default=UNSET)
    repository_selection: Missing[Literal["all", "selected"]] = Field(
        default=UNSET,
        description="Describe whether all repositories have been selected or there's a selection involved",
    )


class AuthenticationTokenPropPermissions(GitHubModel):
    """AuthenticationTokenPropPermissions

    Examples:
        {'issues': 'read', 'deployments': 'write'}
    """


model_rebuild(AuthenticationToken)
model_rebuild(AuthenticationTokenPropPermissions)

__all__ = (
    "AuthenticationToken",
    "AuthenticationTokenPropPermissions",
)
