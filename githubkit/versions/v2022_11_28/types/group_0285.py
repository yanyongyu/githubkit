"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0283 import MetadataType


class ManifestType(TypedDict):
    """Manifest"""

    name: str
    file: NotRequired[ManifestPropFileType]
    metadata: NotRequired[MetadataType]
    resolved: NotRequired[ManifestPropResolvedType]


class ManifestPropFileType(TypedDict):
    """ManifestPropFile"""

    source_location: NotRequired[str]


ManifestPropResolvedType: TypeAlias = dict[str, Any]
"""ManifestPropResolved

A collection of resolved package dependencies.
"""


__all__ = (
    "ManifestPropFileType",
    "ManifestPropResolvedType",
    "ManifestType",
)
