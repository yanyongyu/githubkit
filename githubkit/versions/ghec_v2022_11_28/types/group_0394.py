"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0392 import MetaType


class ScimEnterpriseGroupResponseAllof1Type(TypedDict):
    """ScimEnterpriseGroupResponseAllof1"""

    id: NotRequired[str]
    members: NotRequired[list[ScimEnterpriseGroupResponseAllof1PropMembersItemsType]]
    meta: NotRequired[MetaType]


class ScimEnterpriseGroupResponseAllof1PropMembersItemsType(TypedDict):
    """ScimEnterpriseGroupResponseAllof1PropMembersItems"""

    value: NotRequired[str]
    ref: NotRequired[str]
    display: NotRequired[str]


__all__ = (
    "ScimEnterpriseGroupResponseAllof1PropMembersItemsType",
    "ScimEnterpriseGroupResponseAllof1Type",
)
