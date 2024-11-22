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


class ReposOwnerRepoActionsOidcCustomizationSubPutBody(GitHubModel):
    """Actions OIDC subject customization for a repository

    Actions OIDC subject customization for a repository
    """

    use_default: bool = Field(
        description="Whether to use the default template or not. If `true`, the `include_claim_keys` field is ignored."
    )
    include_claim_keys: Missing[list[str]] = Field(
        default=UNSET,
        description="Array of unique strings. Each claim key can only contain alphanumeric characters and underscores.",
    )


model_rebuild(ReposOwnerRepoActionsOidcCustomizationSubPutBody)

__all__ = ("ReposOwnerRepoActionsOidcCustomizationSubPutBody",)
