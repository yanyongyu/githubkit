"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Literal, Optional
from weakref import ref

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from typing import Literal

    from githubkit import GitHubCore
    from githubkit.response import Response
    from githubkit.typing import Missing
    from githubkit.utils import UNSET

    from ..models import (
        SearchCodeGetResponse200,
        SearchCommitsGetResponse200,
        SearchIssuesGetResponse200,
        SearchLabelsGetResponse200,
        SearchRepositoriesGetResponse200,
        SearchTopicsGetResponse200,
        SearchUsersGetResponse200,
    )
    from ..types import (
        SearchCodeGetResponse200Type,
        SearchCommitsGetResponse200Type,
        SearchIssuesGetResponse200Type,
        SearchLabelsGetResponse200Type,
        SearchRepositoriesGetResponse200Type,
        SearchTopicsGetResponse200Type,
        SearchUsersGetResponse200Type,
    )


class SearchClient:
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

    def code(
        self,
        *,
        q: str,
        sort: Missing[Literal["indexed"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchCodeGetResponse200, SearchCodeGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-code"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchCodeGetResponse200,
            ValidationError,
        )

        url = "/search/code"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCodeGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_code(
        self,
        *,
        q: str,
        sort: Missing[Literal["indexed"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchCodeGetResponse200, SearchCodeGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-code"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchCodeGetResponse200,
            ValidationError,
        )

        url = "/search/code"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCodeGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    def commits(
        self,
        *,
        q: str,
        sort: Missing[Literal["author-date", "committer-date"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchCommitsGetResponse200, SearchCommitsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-commits"""

        from ..models import SearchCommitsGetResponse200

        url = "/search/commits"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCommitsGetResponse200,
        )

    async def async_commits(
        self,
        *,
        q: str,
        sort: Missing[Literal["author-date", "committer-date"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchCommitsGetResponse200, SearchCommitsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-commits"""

        from ..models import SearchCommitsGetResponse200

        url = "/search/commits"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCommitsGetResponse200,
        )

    def issues_and_pull_requests(
        self,
        *,
        q: str,
        sort: Missing[
            Literal[
                "comments",
                "reactions",
                "reactions-+1",
                "reactions--1",
                "reactions-smile",
                "reactions-thinking_face",
                "reactions-heart",
                "reactions-tada",
                "interactions",
                "created",
                "updated",
            ]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchIssuesGetResponse200, SearchIssuesGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-issues-and-pull-requests"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchIssuesGetResponse200,
            ValidationError,
        )

        url = "/search/issues"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchIssuesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_issues_and_pull_requests(
        self,
        *,
        q: str,
        sort: Missing[
            Literal[
                "comments",
                "reactions",
                "reactions-+1",
                "reactions--1",
                "reactions-smile",
                "reactions-thinking_face",
                "reactions-heart",
                "reactions-tada",
                "interactions",
                "created",
                "updated",
            ]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchIssuesGetResponse200, SearchIssuesGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-issues-and-pull-requests"""

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchIssuesGetResponse200,
            ValidationError,
        )

        url = "/search/issues"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchIssuesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    def labels(
        self,
        *,
        repository_id: int,
        q: str,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchLabelsGetResponse200, SearchLabelsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-labels"""

        from ..models import BasicError, SearchLabelsGetResponse200, ValidationError

        url = "/search/labels"

        params = {
            "repository_id": repository_id,
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchLabelsGetResponse200,
            error_models={
                "404": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    async def async_labels(
        self,
        *,
        repository_id: int,
        q: str,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchLabelsGetResponse200, SearchLabelsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-labels"""

        from ..models import BasicError, SearchLabelsGetResponse200, ValidationError

        url = "/search/labels"

        params = {
            "repository_id": repository_id,
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchLabelsGetResponse200,
            error_models={
                "404": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    def repos(
        self,
        *,
        q: str,
        sort: Missing[
            Literal["stars", "forks", "help-wanted-issues", "updated"]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        SearchRepositoriesGetResponse200, SearchRepositoriesGetResponse200Type
    ]:
        """See also: https://docs.github.com/rest/search/search#search-repositories"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchRepositoriesGetResponse200,
            ValidationError,
        )

        url = "/search/repositories"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchRepositoriesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    async def async_repos(
        self,
        *,
        q: str,
        sort: Missing[
            Literal["stars", "forks", "help-wanted-issues", "updated"]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        SearchRepositoriesGetResponse200, SearchRepositoriesGetResponse200Type
    ]:
        """See also: https://docs.github.com/rest/search/search#search-repositories"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchRepositoriesGetResponse200,
            ValidationError,
        )

        url = "/search/repositories"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchRepositoriesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    def topics(
        self,
        *,
        q: str,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchTopicsGetResponse200, SearchTopicsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-topics"""

        from ..models import SearchTopicsGetResponse200

        url = "/search/topics"

        params = {
            "q": q,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchTopicsGetResponse200,
        )

    async def async_topics(
        self,
        *,
        q: str,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchTopicsGetResponse200, SearchTopicsGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-topics"""

        from ..models import SearchTopicsGetResponse200

        url = "/search/topics"

        params = {
            "q": q,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchTopicsGetResponse200,
        )

    def users(
        self,
        *,
        q: str,
        sort: Missing[Literal["followers", "repositories", "joined"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchUsersGetResponse200, SearchUsersGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-users"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchUsersGetResponse200,
            ValidationError,
        )

        url = "/search/users"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchUsersGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    async def async_users(
        self,
        *,
        q: str,
        sort: Missing[Literal["followers", "repositories", "joined"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SearchUsersGetResponse200, SearchUsersGetResponse200Type]:
        """See also: https://docs.github.com/rest/search/search#search-users"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SearchUsersGetResponse200,
            ValidationError,
        )

        url = "/search/users"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchUsersGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )
