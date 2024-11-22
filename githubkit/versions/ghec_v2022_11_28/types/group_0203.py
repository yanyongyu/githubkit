"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class OidcCustomSubRepoType(TypedDict):
    """Actions OIDC subject customization for a repository

    Actions OIDC subject customization for a repository
    """

    use_default: bool
    include_claim_keys: NotRequired[list[str]]


__all__ = ("OidcCustomSubRepoType",)
