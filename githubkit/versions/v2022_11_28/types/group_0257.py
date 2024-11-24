"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0256 import MetadataType


class DependencyType(TypedDict):
    """Dependency"""

    package_url: NotRequired[str]
    metadata: NotRequired[MetadataType]
    relationship: NotRequired[Literal["direct", "indirect"]]
    scope: NotRequired[Literal["runtime", "development"]]
    dependencies: NotRequired[list[str]]


__all__ = ("DependencyType",)
