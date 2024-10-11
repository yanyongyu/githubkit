"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import BaseModel

from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import List, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import Blob, GitRef, GitTag, GitTree, GitCommit, ShortBlob
    from ..types import (
        ReposOwnerRepoGitRefsPostBodyType,
        ReposOwnerRepoGitTagsPostBodyType,
        ReposOwnerRepoGitBlobsPostBodyType,
        ReposOwnerRepoGitTreesPostBodyType,
        ReposOwnerRepoGitCommitsPostBodyType,
        ReposOwnerRepoGitRefsRefPatchBodyType,
        ReposOwnerRepoGitTagsPostBodyPropTaggerType,
        ReposOwnerRepoGitCommitsPostBodyPropAuthorType,
        ReposOwnerRepoGitTreesPostBodyPropTreeItemsType,
        ReposOwnerRepoGitCommitsPostBodyPropCommitterType,
    )


class GitClient:
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

    @overload
    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitBlobsPostBodyType,
    ) -> Response[ShortBlob]: ...

    @overload
    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        content: str,
        encoding: Missing[str] = UNSET,
    ) -> Response[ShortBlob]: ...

    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[ShortBlob]:
        """See also: https://docs.github.com/rest/git/blobs#create-a-blob"""

        from typing import Union

        from ..models import (
            ShortBlob,
            BasicError,
            ValidationError,
            RepositoryRuleViolationError,
            ReposOwnerRepoGitBlobsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/blobs"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitBlobsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": Union[ValidationError, RepositoryRuleViolationError],
            },
        )

    @overload
    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitBlobsPostBodyType,
    ) -> Response[ShortBlob]: ...

    @overload
    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        content: str,
        encoding: Missing[str] = UNSET,
    ) -> Response[ShortBlob]: ...

    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[ShortBlob]:
        """See also: https://docs.github.com/rest/git/blobs#create-a-blob"""

        from typing import Union

        from ..models import (
            ShortBlob,
            BasicError,
            ValidationError,
            RepositoryRuleViolationError,
            ReposOwnerRepoGitBlobsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/blobs"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitBlobsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": Union[ValidationError, RepositoryRuleViolationError],
            },
        )

    def get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Blob]:
        """See also: https://docs.github.com/rest/git/blobs#get-a-blob"""

        from ..models import Blob, BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
                "409": BasicError,
            },
        )

    async def async_get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Blob]:
        """See also: https://docs.github.com/rest/git/blobs#get-a-blob"""

        from ..models import Blob, BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
                "409": BasicError,
            },
        )

    @overload
    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitCommitsPostBodyType,
    ) -> Response[GitCommit]: ...

    @overload
    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        message: str,
        tree: str,
        parents: Missing[List[str]] = UNSET,
        author: Missing[ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Missing[ReposOwnerRepoGitCommitsPostBodyPropCommitterType] = UNSET,
        signature: Missing[str] = UNSET,
    ) -> Response[GitCommit]: ...

    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitCommit]:
        """See also: https://docs.github.com/rest/git/commits#create-a-commit"""

        from ..models import (
            GitCommit,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitCommitsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/commits"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitCommitsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    @overload
    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitCommitsPostBodyType,
    ) -> Response[GitCommit]: ...

    @overload
    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        message: str,
        tree: str,
        parents: Missing[List[str]] = UNSET,
        author: Missing[ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Missing[ReposOwnerRepoGitCommitsPostBodyPropCommitterType] = UNSET,
        signature: Missing[str] = UNSET,
    ) -> Response[GitCommit]: ...

    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitCommit]:
        """See also: https://docs.github.com/rest/git/commits#create-a-commit"""

        from ..models import (
            GitCommit,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitCommitsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/commits"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitCommitsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    def get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitCommit]:
        """See also: https://docs.github.com/rest/git/commits#get-a-commit-object"""

        from ..models import GitCommit, BasicError

        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    async def async_get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitCommit]:
        """See also: https://docs.github.com/rest/git/commits#get-a-commit-object"""

        from ..models import GitCommit, BasicError

        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    def list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[GitRef]]:
        """See also: https://docs.github.com/rest/git/refs#list-matching-references"""

        from typing import List

        from ..models import GitRef, BasicError

        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[GitRef],
            error_models={
                "409": BasicError,
            },
        )

    async def async_list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[GitRef]]:
        """See also: https://docs.github.com/rest/git/refs#list-matching-references"""

        from typing import List

        from ..models import GitRef, BasicError

        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[GitRef],
            error_models={
                "409": BasicError,
            },
        )

    def get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#get-a-reference"""

        from ..models import GitRef, BasicError

        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    async def async_get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#get-a-reference"""

        from ..models import GitRef, BasicError

        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    @overload
    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsPostBodyType,
    ) -> Response[GitRef]: ...

    @overload
    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        ref: str,
        sha: str,
    ) -> Response[GitRef]: ...

    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#create-a-reference"""

        from ..models import (
            GitRef,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitRefsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/refs"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitRefsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    @overload
    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsPostBodyType,
    ) -> Response[GitRef]: ...

    @overload
    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        ref: str,
        sha: str,
    ) -> Response[GitRef]: ...

    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#create-a-reference"""

        from ..models import (
            GitRef,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitRefsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/refs"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitRefsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    def delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/git/refs#delete-a-reference"""

        from ..models import BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    async def async_delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/rest/git/refs#delete-a-reference"""

        from ..models import BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> Response[GitRef]: ...

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        sha: str,
        force: Missing[bool] = UNSET,
    ) -> Response[GitRef]: ...

    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#update-a-reference"""

        from ..models import (
            GitRef,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitRefsRefPatchBody,
        )

        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitRefsRefPatchBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> Response[GitRef]: ...

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        sha: str,
        force: Missing[bool] = UNSET,
    ) -> Response[GitRef]: ...

    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitRef]:
        """See also: https://docs.github.com/rest/git/refs#update-a-reference"""

        from ..models import (
            GitRef,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitRefsRefPatchBody,
        )

        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitRefsRefPatchBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    @overload
    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTagsPostBodyType,
    ) -> Response[GitTag]: ...

    @overload
    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Missing[ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> Response[GitTag]: ...

    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitTag]:
        """See also: https://docs.github.com/rest/git/tags#create-a-tag-object"""

        from ..models import (
            GitTag,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitTagsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/tags"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitTagsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    @overload
    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTagsPostBodyType,
    ) -> Response[GitTag]: ...

    @overload
    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Missing[ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> Response[GitTag]: ...

    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitTag]:
        """See also: https://docs.github.com/rest/git/tags#create-a-tag-object"""

        from ..models import (
            GitTag,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitTagsPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/tags"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitTagsPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
                "409": BasicError,
            },
        )

    def get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitTag]:
        """See also: https://docs.github.com/rest/git/tags#get-a-tag"""

        from ..models import GitTag, BasicError

        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    async def async_get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitTag]:
        """See also: https://docs.github.com/rest/git/tags#get-a-tag"""

        from ..models import GitTag, BasicError

        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "404": BasicError,
                "409": BasicError,
            },
        )

    @overload
    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTreesPostBodyType,
    ) -> Response[GitTree]: ...

    @overload
    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Missing[str] = UNSET,
    ) -> Response[GitTree]: ...

    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitTree]:
        """See also: https://docs.github.com/rest/git/trees#create-a-tree"""

        from ..models import (
            GitTree,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitTreesPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/trees"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitTreesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
                "409": BasicError,
            },
        )

    @overload
    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTreesPostBodyType,
    ) -> Response[GitTree]: ...

    @overload
    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Missing[str] = UNSET,
    ) -> Response[GitTree]: ...

    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[GitTree]:
        """See also: https://docs.github.com/rest/git/trees#create-a-tree"""

        from ..models import (
            GitTree,
            BasicError,
            ValidationError,
            ReposOwnerRepoGitTreesPostBody,
        )

        url = f"/repos/{owner}/{repo}/git/trees"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(ReposOwnerRepoGitTreesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
                "409": BasicError,
            },
        )

    def get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitTree]:
        """See also: https://docs.github.com/rest/git/trees#get-a-tree"""

        from ..models import GitTree, BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "409": BasicError,
            },
        )

    async def async_get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[GitTree]:
        """See also: https://docs.github.com/rest/git/trees#get-a-tree"""

        from ..models import GitTree, BasicError, ValidationError

        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "409": BasicError,
            },
        )
