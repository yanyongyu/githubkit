"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0259 import MetadataType


class SnapshotType(TypedDict):
    """snapshot

    Create a new snapshot of a repository's dependencies.
    """

    version: int
    job: SnapshotPropJobType
    sha: str
    ref: str
    detector: SnapshotPropDetectorType
    metadata: NotRequired[MetadataType]
    manifests: NotRequired[SnapshotPropManifestsType]
    scanned: datetime


class SnapshotPropJobType(TypedDict):
    """SnapshotPropJob"""

    id: str
    correlator: str
    html_url: NotRequired[str]


class SnapshotPropDetectorType(TypedDict):
    """SnapshotPropDetector

    A description of the detector used.
    """

    name: str
    version: str
    url: str


class SnapshotPropManifestsType(TypedDict):
    """SnapshotPropManifests

    A collection of package manifests, which are a collection of related
    dependencies declared in a file or representing a logical group of dependencies.
    """


__all__ = (
    "SnapshotType",
    "SnapshotPropJobType",
    "SnapshotPropDetectorType",
    "SnapshotPropManifestsType",
)
