"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class MetaType(TypedDict):
    """Meta

    The metadata associated with the creation/updates to the user.
    """

    resource_type: Literal["User", "Group"]
    created: NotRequired[str]
    last_modified: NotRequired[str]
    location: NotRequired[str]


__all__ = ("MetaType",)
