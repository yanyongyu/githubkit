"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgActionsVariablesNamePatchBodyType(TypedDict):
    """OrgsOrgActionsVariablesNamePatchBody"""

    name: NotRequired[str]
    value: NotRequired[str]
    visibility: NotRequired[Literal["all", "private", "selected"]]
    selected_repository_ids: NotRequired[list[int]]


__all__ = ("OrgsOrgActionsVariablesNamePatchBodyType",)
