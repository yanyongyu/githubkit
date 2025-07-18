"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class GetCostCenterType(TypedDict):
    """GetCostCenter"""

    id: str
    name: str
    resources: list[GetCostCenterPropResourcesItemsType]


class GetCostCenterPropResourcesItemsType(TypedDict):
    """GetCostCenterPropResourcesItems"""

    type: str
    name: str


__all__ = (
    "GetCostCenterPropResourcesItemsType",
    "GetCostCenterType",
)
