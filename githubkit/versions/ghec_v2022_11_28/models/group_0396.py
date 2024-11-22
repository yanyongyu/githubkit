"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class PatchSchema(GitHubModel):
    """PatchSchema"""

    operations: list[PatchSchemaPropOperationsItems] = Field(
        alias="Operations", description="patch operations list"
    )
    schemas: list[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]] = Field()


class PatchSchemaPropOperationsItems(GitHubModel):
    """PatchSchemaPropOperationsItems"""

    op: Literal["add", "replace", "remove"] = Field()
    path: Missing[str] = Field(default=UNSET)
    value: Missing[str] = Field(
        default=UNSET,
        description="Corresponding 'value' of that field specified by 'path'",
    )


model_rebuild(PatchSchema)
model_rebuild(PatchSchemaPropOperationsItems)

__all__ = (
    "PatchSchema",
    "PatchSchemaPropOperationsItems",
)
