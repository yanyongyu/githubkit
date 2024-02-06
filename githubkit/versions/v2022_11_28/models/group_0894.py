"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgPersonalAccessTokensPostBody(GitHubModel):
    """OrgsOrgPersonalAccessTokensPostBody"""

    action: Literal["revoke"] = Field(
        description="Action to apply to the fine-grained personal access token."
    )
    pat_ids: List[int] = Field(
        max_length=100,
        min_length=1,
        description="The IDs of the fine-grained personal access tokens.",
    )


model_rebuild(OrgsOrgPersonalAccessTokensPostBody)

__all__ = ("OrgsOrgPersonalAccessTokensPostBody",)
