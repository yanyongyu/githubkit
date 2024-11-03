"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class PatchSchemaType(TypedDict):
    """PatchSchema"""

    operations: list[PatchSchemaPropOperationsItemsType]
    schemas: list[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]]


class PatchSchemaPropOperationsItemsType(TypedDict):
    """PatchSchemaPropOperationsItems"""

    op: Literal["add", "replace", "remove"]
    path: NotRequired[str]
    value: NotRequired[str]


__all__ = (
    "PatchSchemaType",
    "PatchSchemaPropOperationsItemsType",
)
