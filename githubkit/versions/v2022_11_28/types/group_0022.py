"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0021 import ScopedInstallationType


class AuthorizationType(TypedDict):
    """Authorization

    The authorization for an OAuth app, GitHub App, or a Personal Access Token.
    """

    id: int
    url: str
    scopes: Union[list[str], None]
    token: str
    token_last_eight: Union[str, None]
    hashed_token: Union[str, None]
    app: AuthorizationPropAppType
    note: Union[str, None]
    note_url: Union[str, None]
    updated_at: datetime
    created_at: datetime
    fingerprint: Union[str, None]
    user: NotRequired[Union[None, SimpleUserType]]
    installation: NotRequired[Union[None, ScopedInstallationType]]
    expires_at: Union[datetime, None]


class AuthorizationPropAppType(TypedDict):
    """AuthorizationPropApp"""

    client_id: str
    name: str
    url: str


__all__ = (
    "AuthorizationPropAppType",
    "AuthorizationType",
)
