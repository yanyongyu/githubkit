"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, overload
from weakref import ref

from pydantic import BaseModel

from githubkit.compat import model_dump, type_validate_python
from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from datetime import datetime

    from githubkit import GitHubCore
    from githubkit.response import Response
    from githubkit.typing import Missing
    from githubkit.utils import UNSET

    from ..models import (
        DependencyGraphDiffItems,
        DependencyGraphSpdxSbom,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
    )
    from ..types import (
        DependencyGraphDiffItemsType,
        DependencyGraphSpdxSbomType,
        MetadataType,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
        SnapshotPropDetectorType,
        SnapshotPropJobType,
        SnapshotPropManifestsType,
        SnapshotType,
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
        *,
        name: Missing[str] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[DependencyGraphDiffItems], list[DependencyGraphDiffItemsType]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/dependency-review#get-a-diff-of-the-dependencies-between-commits"""

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
            response_model=list[DependencyGraphDiffItems],
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
        *,
        name: Missing[str] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[DependencyGraphDiffItems], list[DependencyGraphDiffItemsType]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/dependency-review#get-a-diff-of-the-dependencies-between-commits"""

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
            response_model=list[DependencyGraphDiffItems],
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
        headers: Optional[dict[str, str]] = None,
    ) -> Response[DependencyGraphSpdxSbom, DependencyGraphSpdxSbomType]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository"""

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
        headers: Optional[dict[str, str]] = None,
    ) -> Response[DependencyGraphSpdxSbom, DependencyGraphSpdxSbomType]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository"""

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
        headers: Optional[dict[str, str]] = None,
        data: SnapshotType,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]: ...

    @overload
    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]: ...

    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[SnapshotType] = UNSET,
        **kwargs,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/dependency-submission#create-a-snapshot-of-dependencies-for-a-repository"""

        from ..models import (
            ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
            Snapshot,
        )

        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
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
        headers: Optional[dict[str, str]] = None,
        data: SnapshotType,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]: ...

    @overload
    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]: ...

    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[SnapshotType] = UNSET,
        **kwargs,
    ) -> Response[
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/dependency-graph/dependency-submission#create-a-snapshot-of-dependencies-for-a-repository"""

        from ..models import (
            ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
            Snapshot,
        )

        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(Snapshot, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )
