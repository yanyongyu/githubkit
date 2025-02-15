"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OidcCustomSub(GitHubModel):
    """Actions OIDC Subject customization

    Actions OIDC Subject customization
    """

    include_claim_keys: list[str] = Field(
        description="Array of unique strings. Each claim key can only contain alphanumeric characters and underscores."
    )


model_rebuild(OidcCustomSub)

__all__ = ("OidcCustomSub",)
