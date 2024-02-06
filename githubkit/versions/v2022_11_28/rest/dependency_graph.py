"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import BaseModel

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import List
    from datetime import datetime

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        DependencyGraphSpdxSbom,
        DependencyGraphDiffItems,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
    )
    from ..types import (
        MetadataType,
        SnapshotType,
        SnapshotPropJobType,
        SnapshotPropDetectorType,
        SnapshotPropManifestsType,
    )


class DependencyGraphClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def diff_range(
        self,
        owner: str,
        repo: str,
        basehead: str,
        name: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[DependencyGraphDiffItems]]:
        """See also: https://docs.github.com/rest/dependency-graph/dependency-review#get-a-diff-of-the-dependencies-between-commits"""

        from typing import List

        from ..models import BasicError, DependencyGraphDiffItems

        url = f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"

        params = {
            "name": name,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[DependencyGraphDiffItems],
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    async def async_diff_range(
        self,
        owner: str,
        repo: str,
        basehead: str,
        name: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[DependencyGraphDiffItems]]:
        """See also: https://docs.github.com/rest/dependency-graph/dependency-review#get-a-diff-of-the-dependencies-between-commits"""

        from typing import List

        from ..models import BasicError, DependencyGraphDiffItems

        url = f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"

        params = {
            "name": name,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[DependencyGraphDiffItems],
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    def export_sbom(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[DependencyGraphSpdxSbom]:
        """See also: https://docs.github.com/rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository"""

        from ..models import BasicError, DependencyGraphSpdxSbom

        url = f"/repos/{owner}/{repo}/dependency-graph/sbom"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=DependencyGraphSpdxSbom,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    async def async_export_sbom(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[DependencyGraphSpdxSbom]:
        """See also: https://docs.github.com/rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository"""

        from ..models import BasicError, DependencyGraphSpdxSbom

        url = f"/repos/{owner}/{repo}/dependency-graph/sbom"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=DependencyGraphSpdxSbom,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: SnapshotType,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]: ...

    @overload
    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]: ...

    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[SnapshotType] = UNSET,
        **kwargs,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]:
        """See also: https://docs.github.com/rest/dependency-graph/dependency-submission#create-a-snapshot-of-dependencies-for-a-repository"""

        from ..models import (
            Snapshot,
            ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )

        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(Snapshot, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )

    @overload
    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: SnapshotType,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]: ...

    @overload
    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]: ...

    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[SnapshotType] = UNSET,
        **kwargs,
    ) -> Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]:
        """See also: https://docs.github.com/rest/dependency-graph/dependency-submission#create-a-snapshot-of-dependencies-for-a-repository"""

        from ..models import (
            Snapshot,
            ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )

        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(Snapshot, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )
