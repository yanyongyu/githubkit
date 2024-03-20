"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Dict, Optional


from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from typing import List
    from datetime import date

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import Root, ApiOverview


class MetaClient:
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

    def root(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Root]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#github-api-root"""

        from ..models import Root

        url = "/"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Root,
        )

    async def async_root(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Root]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#github-api-root"""

        from ..models import Root

        url = "/"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Root,
        )

    def get(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ApiOverview]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-apiname-meta-information"""

        from ..models import ApiOverview

        url = "/meta"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ApiOverview,
        )

    async def async_get(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ApiOverview]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-apiname-meta-information"""

        from ..models import ApiOverview

        url = "/meta"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ApiOverview,
        )

    def get_octocat(
        self,
        s: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[str]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-octocat"""

        url = "/octocat"

        params = {
            "s": s,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=str,
        )

    async def async_get_octocat(
        self,
        s: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[str]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-octocat"""

        url = "/octocat"

        params = {
            "s": s,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=str,
        )

    def get_all_versions(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[date]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-all-api-versions"""

        from typing import List
        from datetime import date

        from ..models import BasicError

        url = "/versions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[date],
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_all_versions(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[date]]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-all-api-versions"""

        from typing import List
        from datetime import date

        from ..models import BasicError

        url = "/versions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[date],
            error_models={
                "404": BasicError,
            },
        )

    def get_zen(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[str]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-the-zen-of-github"""

        url = "/zen"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=str,
        )

    async def async_get_zen(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[str]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/meta/meta#get-the-zen-of-github"""

        url = "/zen"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=str,
        )
