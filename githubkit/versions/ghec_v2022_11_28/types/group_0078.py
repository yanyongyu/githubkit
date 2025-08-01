"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0074 import DependabotAlertPackageType


class DependabotAlertWithRepositoryPropDependencyType(TypedDict):
    """DependabotAlertWithRepositoryPropDependency

    Details for the vulnerable dependency.
    """

    package: NotRequired[DependabotAlertPackageType]
    manifest_path: NotRequired[str]
    scope: NotRequired[Union[None, Literal["development", "runtime"]]]
    relationship: NotRequired[
        Union[None, Literal["unknown", "direct", "transitive", "inconclusive"]]
    ]


__all__ = ("DependabotAlertWithRepositoryPropDependencyType",)
