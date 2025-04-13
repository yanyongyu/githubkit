"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrgsOrgCodespacesSecretsGetResponse200Type(TypedDict):
    """OrgsOrgCodespacesSecretsGetResponse200"""

    total_count: int
    secrets: list[CodespacesOrgSecretType]


class CodespacesOrgSecretType(TypedDict):
    """Codespaces Secret

    Secrets for a GitHub Codespace.
    """

    name: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: NotRequired[str]


__all__ = (
    "CodespacesOrgSecretType",
    "OrgsOrgCodespacesSecretsGetResponse200Type",
)
