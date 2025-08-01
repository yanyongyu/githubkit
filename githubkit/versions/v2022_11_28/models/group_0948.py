"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild

from .group_0121 import CustomProperty


class OrgsOrgPropertiesSchemaPatchBody(GitHubModel):
    """OrgsOrgPropertiesSchemaPatchBody"""

    properties: list[CustomProperty] = Field(
        max_length=100 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        description="The array of custom properties to create or update.",
    )


model_rebuild(OrgsOrgPropertiesSchemaPatchBody)

__all__ = ("OrgsOrgPropertiesSchemaPatchBody",)
