"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class CredentialAuthorization(GitHubModel):
    """Credential Authorization

    Credential Authorization
    """

    login: str = Field(description="User login that owns the underlying credential.")
    credential_id: int = Field(description="Unique identifier for the credential.")
    credential_type: str = Field(
        description="Human-readable description of the credential type."
    )
    token_last_eight: Missing[str] = Field(
        default=UNSET,
        description="Last eight characters of the credential. Only included in responses with credential_type of personal access token.",
    )
    credential_authorized_at: datetime = Field(
        description="Date when the credential was authorized for use."
    )
    scopes: Missing[List[str]] = Field(
        default=UNSET, description="List of oauth scopes the token has been granted."
    )
    fingerprint: Missing[str] = Field(
        default=UNSET,
        description="Unique string to distinguish the credential. Only included in responses with credential_type of SSH Key.",
    )
    credential_accessed_at: Union[datetime, None] = Field(
        description="Date when the credential was last accessed. May be null if it was never accessed"
    )
    authorized_credential_id: Union[int, None] = Field()
    authorized_credential_title: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The title given to the ssh key. This will only be present when the credential is an ssh key.",
    )
    authorized_credential_note: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The note given to the token. This will only be present when the credential is a token.",
    )
    authorized_credential_expires_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="The expiry for the token. This will only be present when the credential is a token.",
    )


model_rebuild(CredentialAuthorization)

__all__ = ("CredentialAuthorization",)
