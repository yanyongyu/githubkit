"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class OrganizationCustomRepositoryRoleUpdateSchemaType(TypedDict):
    """OrganizationCustomRepositoryRoleUpdateSchema"""

    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    base_role: NotRequired[Literal["read", "triage", "write", "maintain"]]
    permissions: NotRequired[List[str]]


__all__ = ("OrganizationCustomRepositoryRoleUpdateSchemaType",)