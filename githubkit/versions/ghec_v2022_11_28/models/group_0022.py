"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0021 import ScopedInstallation


class Authorization(GitHubModel):
    """Authorization

    The authorization for an OAuth app, GitHub App, or a Personal Access Token.
    """

    id: int = Field()
    url: str = Field()
    scopes: Union[list[str], None] = Field(
        description="A list of scopes that this authorization is in."
    )
    token: str = Field()
    token_last_eight: Union[str, None] = Field()
    hashed_token: Union[str, None] = Field()
    app: AuthorizationPropApp = Field()
    note: Union[str, None] = Field()
    note_url: Union[str, None] = Field()
    updated_at: datetime = Field()
    created_at: datetime = Field()
    fingerprint: Union[str, None] = Field()
    user: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    installation: Missing[Union[None, ScopedInstallation]] = Field(default=UNSET)
    expires_at: Union[datetime, None] = Field()


class AuthorizationPropApp(GitHubModel):
    """AuthorizationPropApp"""

    client_id: str = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(Authorization)
model_rebuild(AuthorizationPropApp)

__all__ = (
    "Authorization",
    "AuthorizationPropApp",
)
